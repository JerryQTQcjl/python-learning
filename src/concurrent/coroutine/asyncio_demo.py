#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/10 15:58"

import asyncio
from time import sleep


async def hello(name):
    """
    定义协程，这玩意不是一个函数，而是一个协程对象，类似生成器，不会直接执行而是需要事件循环触发后才会执行
    """
    print(f"hello {name}")
    await asyncio.sleep(1)
    print("hello again")
    return f"hello {name}"


async def main():
    # print(asyncio.get_running_loop())
    # L = await asyncio.gather(hello("Jerry"), hello("Yilibao"))
    # print(L)
    task = asyncio.create_task(hello("Jerry"))
    print(await task)


if __name__ == "__main__":
    print(hello("Jerry"))
    # asyncio.run(main())
