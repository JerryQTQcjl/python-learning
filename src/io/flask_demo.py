#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/15 17:47"

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!111'

if __name__ == '__main__':
    # 将端口设置为6688
    app.run(port=6688)
