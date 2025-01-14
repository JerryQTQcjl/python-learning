#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/20 16:10"


def refresh_token(access_token) :

    import json
    import random
    import requests
    import time

    interface = 'oauth/token'
    url = 'https://api.e.qq.com/v3.0/' + interface

    common_parameters = {
        'access_token': access_token,
        'timestamp': int(time.time()),
        'nonce': str(time.time()) + str(random.randint(0, 999999)),
    }

    parameters = {
        "client_id": "1111332569",
        "client_secret": "y0svj94RPmk95ZzO",
        "grant_type": "refresh_token",
        "refresh_token": "4e4a5f8b32cb5ecaa6ffefc8fae4bf75"
    }

    parameters.update(common_parameters)
    for k in parameters:
        if type(parameters[k]) is not str:
            parameters[k] = json.dumps(parameters[k])

    r = requests.get(url, params = parameters)

    return r.json()


if __name__ == "__main__":
    print(refresh_token("31ae4f96f412907aef19c52459466e15"))