#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/7 00:29"

# multithread
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        # try:
        #     lock.acquire()
            change_it(n)
        # finally:
        #     lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t3 = threading.Thread(target=run_thread, args=(1,))
    t4 = threading.Thread(target=run_thread, args=(3,))
    t5 = threading.Thread(target=run_thread, args=(6,))
    t6 = threading.Thread(target=run_thread, args=(9,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    print(balance)
