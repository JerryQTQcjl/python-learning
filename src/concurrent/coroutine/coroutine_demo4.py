#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: coroutine_demo4.py
@Author: Jerry Chan
@Created: 2025-08-11 12:45
@Description: 模拟基于yield + io多路复用的的协程调度
"""

"""
Mini asyncio: generator-based coroutines + selectors + non-blocking socket
Python 3.8+
"""
import socket, selectors, types, time, heapq, collections

# ===== 协程“系统调用” =====
class Sleep:
    def __init__(self, delay):
        self.when = time.time() + delay

class ReadWait:
    def __init__(self, sock):
        self.sock = sock

class WriteWait:
    def __init__(self, sock):
        self.sock = sock


# ===== 调度器（事件循环）=====
class Scheduler:
    def __init__(self):
        self.ready = collections.deque()     # 就绪任务队列
        self.sleeping = []                   # 小根堆: (when, task)
        self.selector = selectors.DefaultSelector()
        self.wait_for_read = {}              # sock -> task
        self.wait_for_write = {}             # sock -> task

    def new_task(self, gen):
        self.ready.append(Task(gen))

    def run(self):
        while self.ready or self.sleeping or self.wait_for_read or self.wait_for_write:
            # 1) 唤醒到期的睡眠任务
            now = time.time()
            while self.sleeping and self.sleeping[0][0] <= now:
                _, task = heapq.heappop(self.sleeping)
                self.ready.append(task)

            # 2) 没有就绪任务？阻塞在 I/O 或最近的定时器
            timeout = None
            if not self.ready:
                if self.sleeping:
                    timeout = max(0, self.sleeping[0][0] - time.time())
                # 等待 I/O 就绪或超时（最近的睡眠）
                if self.wait_for_read or self.wait_for_write:
                    events = self.selector.select(timeout)
                    for key, mask in events:
                        sock = key.fileobj
                        # 将对应任务移回 ready
                        if mask & selectors.EVENT_READ and sock in self.wait_for_read:
                            task = self.wait_for_read.pop(sock)
                            self.selector.unregister(sock)
                            self.ready.append(task)
                        if mask & selectors.EVENT_WRITE and sock in self.wait_for_write:
                            task = self.wait_for_write.pop(sock)
                            # 可能前面已经 unregister 了，避免重复
                            try:
                                self.selector.unregister(sock)
                            except Exception:
                                pass
                            self.ready.append(task)
                else:
                    # 没 I/O，只睡到下一个定时器
                    if timeout is not None:
                        time.sleep(timeout)
                    # 再次循环会把到期的唤醒
                    continue

            # 3) 取一个就绪任务继续执行到下一个 yield
            if not self.ready:
                continue
            task = self.ready.popleft()
            try:
                req = task.step()  # -> 下一个系统调用对象
            except StopIteration:
                continue  # 任务结束

            # 4) 处理系统调用
            if isinstance(req, Sleep):
                heapq.heappush(self.sleeping, (req.when, task))
            elif isinstance(req, ReadWait):
                sock = req.sock
                sock.setblocking(False)
                self.wait_for_read[sock] = task
                self.selector.register(sock, selectors.EVENT_READ, data=None)
            elif isinstance(req, WriteWait):
                sock = req.sock
                sock.setblocking(False)
                self.wait_for_write[sock] = task
                self.selector.register(sock, selectors.EVENT_WRITE, data=None)
            else:
                raise RuntimeError(f"Unknown syscall: {req!r}")


class Task:
    def __init__(self, gen):
        self.gen = gen

    def step(self, value=None, exc=None):
        if exc is not None:
            return self.gen.throw(exc)
        return self.gen.send(value)


# ====== 一些基于“系统调用”的协程工具 ======
def sleep(delay):
    # 生成器协程：yield Sleep
    yield Sleep(delay)

def connect(host, port, timeout=5.0):
    # 非阻塞 connect；返回已连接的 socket
    # 1) 解析地址
    infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    af, socktype, proto, _, addr = infos[0]
    sock = socket.socket(af, socktype, proto)
    sock.setblocking(False)

    try:
        sock.connect(addr)
    except BlockingIOError:
        pass

    # 2) 等待可写（连接建立或失败）
    start = time.time()
    while True:
        yield WriteWait(sock)
        # 检查是否连接成功
        err = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        if err == 0:
            break
        # 部分平台 err 可能为非零表示还没好，或者直接抛异常也行
        if time.time() - start > timeout:
            sock.close()
            raise TimeoutError("connect timeout")
    return sock

def send_all(sock, data):
    # 非阻塞写直到全部发送
    view = memoryview(data)
    total = 0
    while total < len(data):
        try:
            sent = sock.send(view[total:])
            if sent == 0:
                raise ConnectionError("socket closed while sending")
            total += sent
        except (BlockingIOError, InterruptedError):
            yield WriteWait(sock)
    return total

def recv_some(sock, max_bytes=4096):
    while True:
        try:
            chunk = sock.recv(max_bytes)
            return chunk
        except (BlockingIOError, InterruptedError):
            yield ReadWait(sock)

def recv_until_close(sock, chunk_size=4096):
    # 边读边 yield control；直到对端关闭
    buf = bytearray()
    while True:
        chunk = (yield from recv_some(sock, chunk_size))
        if not chunk:
            break
        buf += chunk
    return bytes(buf)


# ====== Demo：并发抓两个站点的首页字节数 ======
def fetch_http(host, path="/", port=80):
    # 极简 HTTP/1.0 GET，演示 I/O 调度，不处理 HTTPS
    sock = (yield from connect(host, port))
    request = f"GET {path} HTTP/1.0\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode()
    yield from send_all(sock, request)
    data = (yield from recv_until_close(sock))
    sock.close()
    print(f"[{host}{path}] got {len(data)} bytes")
    # print(f"[{host}{path}] {data}")

    

def main():
    # 演示 I/O + 定时器交替
    print("start...")
    yield from sleep(0.1)  # 给调度器点面子
    yield from fetch_http("www.baidu.com", "/")
    yield from fetch_http("www.sina.com.cn", "/")
    print("done")

# 也可以完全并发（两个请求同时飞）
def main_concurrent():
    # 这个 main 本身只是个“启动器”，真正并发靠调度器 new_task 多个协程
    print("concurrent start...")
    yield from sleep(5)
    print("concurrent launcher done")  # 启动器结束并不影响其他任务继续


if __name__ == "__main__":
    # 方案1：串并结合，按 main 顺序跑两个 fetch
    sched = Scheduler()
    sched.new_task(main())
    sched.run()

    # 方案2：真正并发：两个 fetch + 一个小启动器
    print("\n=== real concurrent ===")
    sched = Scheduler()
    sched.new_task(main_concurrent())
    sched.new_task(fetch_http("www.baidu.com", "/"))
    sched.new_task(fetch_http("www.sina.com.cn", "/"))
    sched.run()
