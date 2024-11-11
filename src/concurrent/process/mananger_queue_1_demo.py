#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/9 13:50"

from multiprocessing.managers import BaseManager
import queue
import random

# 发送任务
task_queue = queue.Queue()

# 接收任务
result_queue = queue.Queue()

# 继承
class QueueManager(BaseManager):
    pass

def task_q():
    return task_queue

def result_q():
    return result_queue


if __name__ == '__main__':
    # 注册队列
    BaseManager.register('get_task_queue', callable=task_q)
    BaseManager.register('get_result_queue', callable=result_q)

    # 绑定端口和验证密钥
    manager = BaseManager(address=('127.0.0.1', 8082), authkey=b'abc')
    manager.start()

    # 获取队列
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放入任务
    for i in range(10):
        n = random.randint(0, 10000)
        print(f'Put task {n}...')
        task.put(n)

    # 获取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print(f'Result: {r}')

    # 关闭
    manager.shutdown()
    print('master exit.')

