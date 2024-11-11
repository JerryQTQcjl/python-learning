#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ 元类，在创建类信息是可以动态的修改类信息 """
__date__ = "2024/10/4 12:07"

import http
from http.client import HTTPConnection

class HttpClientMetaClass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'HttpClient':
            return type.__new__(cls, name, bases, attrs)
        apis = {k: v for k, v in attrs.items() if isinstance(v, Api)}
        for k, v in apis.items():
            attrs[k] = lambda self: HttpClient.execute(v)
        return type.__new__(cls, name, bases, attrs)

class Api(object):

    def __init__(self, url, path='/', method='GET', headers={}, body=None):
        self.url = url
        self.path = path
        self.method = method
        self.headers = headers
        self.body = body

    def __str__(self):
        return f'Request(url={self.url}, method={self.method}, headers={self.headers}, body={self.body})'

class HttpClient(object, metaclass=HttpClientMetaClass):

    def execute(api):
        _conn = http.client.HTTPConnection(api.url)
        _conn.request(api.method, api.path, api.body, api.headers)
        _response = _conn.getresponse()
        _result = _response.read()
        _conn.close()
        return _result

class BaiduSdk(HttpClient):
    index = Api('www.baidu.com')

if __name__ == "__main__":
    sdk = BaiduSdk()
    print(sdk.index())
