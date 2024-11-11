#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/10 15:58"

import asyncio
from time import sleep

async def hello(name):
    print(f'hello {name}')
    await asyncio.sleep(1)
    print('hello again')
    return f'hello {name}'

async def main():
    # print(asyncio.get_running_loop())
    # L = await asyncio.gather(hello("Jerry"), hello("Yilibao"))
    # print(L)
    task = asyncio.create_task(hello("Jerry"))
    print(await task)

if __name__ == "__main__":
    asyncio.run(main())
