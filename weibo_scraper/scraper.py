#!/usr/bin/python3
# encoding: utf-8
# Author: fanxn
# Date: 2018/4/22

import urllib.request as request
from traceback import format_exc

main_page = "https://weibo.com/"


def plain_get(url):
    try:
        with request.urlopen(url) as rep:
            cont = rep.read().decode('gb2312')
        return cont
    except Exception as e:
        format_exc()


def post_req(url, data=b''):
    req = request.Request(url, data=data, method="POST")
    return plain_get(req)


if __name__ == "__main__":
    print(post_req(main_page))
