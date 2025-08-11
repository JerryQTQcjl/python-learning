#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: coroutine_demo3.py
@Author: Jerry Chan
@Created: 2025-08-11 11:51
@Description: gpt5 生成基于 yield 的协程事件循环
"""

import time, heapq, collections

class Sleep:
    def __init__(self, delay):
        self.when = time.time() + delay

class Task:
    def __init__(self, gen):
        self.gen = gen  # 生成器协程

class Scheduler:
    def __init__(self):
        self.ready = collections.deque()
        self.sleeping = []  # [(when, task)]

    def new_task(self, gen):
        self.ready.append(Task(gen))

    def run(self):
        while self.ready or self.sleeping:
            # 先把到点儿的唤醒
            now = time.time()
            while self.sleeping and self.sleeping[0][0] <= now:
                _, task = heapq.heappop(self.sleeping)
                self.ready.append(task)

            if not self.ready:
                # 没就绪任务，就睡到最近的那个唤醒点
                when, task = heapq.heappop(self.sleeping)
                time.sleep(max(0, when - time.time()))
                self.ready.append(task)

            task = self.ready.popleft()
            try:
                req = task.gen.send(None)  # 继续执行到下一个 yield
            except StopIteration:
                continue  # 任务结束
            # 处理“系统调用”
            if isinstance(req, Sleep):
                heapq.heappush(self.sleeping, (req.when, task))
            else:
                raise RuntimeError(f"unknown syscall: {req!r}")

# === 示例：两个协程交替运行 ===
def worker(name):
    for i in range(3):
        print(f"{name} step {i}")
        yield Sleep(0.5)
    print(f"{name} done")

sched = Scheduler()
sched.new_task(worker("A"))
sched.new_task(worker("B"))
sched.run()
