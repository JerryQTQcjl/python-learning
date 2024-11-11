#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/10 14:27"

# n = yield r 先执行，然后yield r，等待send(n)的调用，才会来到 n = yield
# 解释执行步骤
# 1. 调用consumer()函数，创建一个generator对象c
# 2. 调用c.send(None)，启动生成器
# 3. 执行到yield r，consumer函数暂停，返回r的值 (可见先执行 yield r)
# 4. producer函数继续执行，执行到yield n (可见后执行 n = yield)
# 5. 回到consumer函数，consumer函数继续执行，执行到r = '200 OK'
# 6. consumer函数返回r的值'200 OK'
# 7. 回到produce函数，produce函数继续执行，执行到r = c.send(n)
# 8. 回到consumer函数，consumer函数继续执行，执行到yield r
#
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    i= c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)
