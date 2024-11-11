#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 异常捕获 """
__date__ = "2024/10/20 23:54"

import threading
import traceback

if __name__ == "__main__":
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ValueError as e:
        print(f'Thread[{threading.get_ident()}] ValueError:{e} \n {traceback.format_exc()}')
    except ZeroDivisionError as e:
        # threading.get_ident() 获取线程信息
        # traceback.format_exc() 获取异常堆栈
        print(f'Thread[{threading.get_ident()}] ZeroDivisionError:{e} \n {traceback.format_exc()}')
    else:
        # 如果没有异常会走到这个分支
        print('no error!')
    finally:
        print('finally...')
        print('END')
