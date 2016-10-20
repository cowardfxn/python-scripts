#!/usr/bin/python
# encoding: utf-8

'''
gevent使用测试

'''

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib.request as request
import json


def fetch(pid):
    response = request.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print("Process {0}: {1}".format(pid, datetime))
    return datetime

def synchronous():
    for i in range(1, 10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


if __name__ == "__main__":
    print("Synchronous:\n")
    synchronous()

    print("-----------\n")
    print("Asynchronous:\n")
    asynchronous()
