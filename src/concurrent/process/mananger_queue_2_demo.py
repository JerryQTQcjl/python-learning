#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/9 13:50"

import _queue
from multiprocessing.managers import BaseManager
import time

# 创建QueueManager:
class QueueManager(BaseManager):
    pass

# 注册队列
BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

if __name__ == "__main__":
    # 连接到服务器
    server_addr = '127.0.0.1'
    print(f'Connect to server {server_addr}...')

    # 连接
    m = BaseManager(address=(server_addr, 8082), authkey=b'abc')
    m.connect()

    # 获取队列
    task = m.get_task_queue()
    result = m.get_result_queue()

    # 处理任务
    for i in range(10):
        try:
            n = task.get(timeout=1)  # 增加超时时间
            print(f'Run task {n} * {n}...')
            r = f'{n} * {n} = {n * n}'
            time.sleep(1)
            result.put(r)
        except _queue.Empty:
            print('Task queue is empty.')

    print('worker exit.')

