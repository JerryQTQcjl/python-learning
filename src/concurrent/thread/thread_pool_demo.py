#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/7 00:17"


import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def square(n):
    sleep(5)
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with ThreadPoolExecutor(max_workers = 3) as executor:
        futures = [executor.submit(square, num) for num in numbers]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"An error occurred: {e}")