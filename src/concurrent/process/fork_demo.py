#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 使用操作系统的 fork """
__date__ = "2024/10/21 00:26"

import os

if __name__ == "__main__":
    pid = os.fork()
    if pid == 0:
        print(f"child process, parent pid: {pid}")
    else:
        print(f"parent process, child pid: {pid}")

