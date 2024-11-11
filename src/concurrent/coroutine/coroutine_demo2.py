#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ gpt 生成的  """
__date__ = "2024/11/11 00:56"

import time
from collections import deque

class SimpleEventLoop:
    def __init__(self):
        self.tasks = deque()

    def create_task(self, coro):
        self.tasks.append(coro)

    def run_forever(self):
        while self.tasks:
            task = self.tasks.popleft()
            try:
                next(task)
                self.tasks.append(task)
            except StopIteration:
                pass

def sleep(duration):
    start = time.time()
    while time.time() - start < duration:
        yield

def fetch_data(delay, data):
    print(f'Start fetching {data}...')
    yield from sleep(delay)
    print(f'Done fetching {data}')

def main():
    loop.create_task(fetch_data(2, 'data1'))
    loop.create_task(fetch_data(3, 'data2'))
    loop.create_task(fetch_data(1, 'data3'))

# 创建事件循环并运行
loop = SimpleEventLoop()
main()  # 直接调用main来添加任务
loop.run_forever()



