#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """  """
__date__ = "2024/10/21 01:01"

import os
import time
from multiprocessing import Pool

def dosomething(x):
    print(f'child process start, parent pid: {os.getppid()}, child pid: {os.getpid()}')
    start = time.time()
    time.sleep(3)
    print(f'child process result: {x}')
    print(f'child process end, child pid: {os.getpid()}, cost:{time.time() - start}')
    return x * x

if __name__ == "__main__":
    print('parent process start')
    pool = Pool(4)
    for i in range(5):
        pool.apply_async(dosomething, args=(i,))
    # close 之后就无法在提交任务，否则会报错，这样看着是 pool 是无法复用的，除非使用其他方法阻塞等待
    pool.close()
    # join 必须在 close 之后调用，阻塞等待进程执行完成
    pool.join()
    # time.sleep(10)
    print('parent process end')
