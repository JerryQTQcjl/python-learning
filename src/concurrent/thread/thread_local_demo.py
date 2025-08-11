#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/9 11:38"

import threading
from time import sleep

thread_local_user = threading.local()

def hello():
    print(f'{thread_local_user.hello}, {thread_local_user.name}')

def process_user(name, hi='hello'):
    thread_local_user.hello = hi
    thread_local_user.name = name
    hello()

if __name__ == "__main__":
    threading.Thread(target=process_user, args=('jerry','hi',)).start()
    threading.Thread(target=process_user, args=('yilibao',)).start()
    sleep(1)

