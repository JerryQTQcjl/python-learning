#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/11/20 16:00"

def lead_clues_get(access_token) :

    import random
    import requests
    import time

    interface = 'lead_clues/get'
    url = 'https://api.e.qq.com/' + interface

    common_parameters = {
        'access_token': access_token,
        'timestamp': int(time.time()),
        'nonce': str(time.time()) + str(random.randint(0, 999999)),
    }

    parameters = {
        "account_id": 50086486,
        "time_range":
            {
                "start_time": 1732019035,
                "end_time": 1732105435,
                "time_type": "TIME_TYPE_ACTION_TIME"
            },
        "page": 1,
        "page_size": 20
    }
    r = requests.post(url, params = common_parameters, json = parameters)

    return r.json()

def refresh_token(access_token) :

    import json
    import random
    import requests
    import time

    interface = 'oauth/token'
    url = 'https://api.e.qq.com/v1.3/' + interface

    common_parameters = {
        'access_token': None,
        'timestamp': int(time.time()),
        'nonce': str(time.time()) + str(random.randint(0, 999999)),
    }

    parameters = {
        "client_id": "1111332551",
        "client_secret": "j0pzxYYJnWBKa5N2",
        "grant_type": "refresh_token",
        "refresh_token": "45809f94095557bf116d99da2c163b5e"
    }

    parameters.update(common_parameters)
    for k in parameters:
        if type(parameters[k]) is not str:
            parameters[k] = json.dumps(parameters[k])

    r = requests.get(url, params = parameters)

    return r.json()

if __name__ == "__main__":
    # access_token = '00733a98b201e8dff2feb4d0ae7184f7'
    # r = lead_clues_get(access_token)
    # print(r)
    print(refresh_token("31ae4f96f412907aef19c52459466e15"))