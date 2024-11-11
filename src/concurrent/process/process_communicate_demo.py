#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/10/31 01:01"

import os
import random
from multiprocessing import Queue
from multiprocessing.context import Process
from time import sleep

def produce(q: Queue):
    print(f'producer({os.getpid()}) start')
    i = 0
    while i < 10:
        i += 1
        msg = random.randint(0, 10)
        q.put(msg)
        print(f'produce {msg}')
        sleep(random.randint(0, 1))

def consume(q: Queue):
    print(f'consumer({os.getpid()}) start')
    while True:
        msg = q.get()
        print(f'consume {msg}')

if __name__ == "__main__":
    q = Queue()
    p = Process(target=produce, args=(q,))
    c = Process(target=consume, args=(q,))

    c.start()
    p.start()

    p.join()
    c.terminate()
