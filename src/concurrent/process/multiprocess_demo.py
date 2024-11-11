#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/10/21 00:45"

import multiprocessing
import os
from traceback import print_last

def process_func(p):
    print(f'child process, parent pid: {p}, child pid: {os.getpid()}')

if __name__ == "__main__":
    print('parent process start')
    # lambda 不支持 pickle 序列化（因为是匿名函数）
    # pr = multiprocessing.Process(target=lambda p: print(f'child process, parent pid: {p}, child pid: {os.getpid()}'), args=(os.getpid(),))
    pr = multiprocessing.Process(target=process_func, args=(os.getpid(),))
    pr.start()
    pr.join()
    print('parent process end')
