#!/usr/bin/python
# encoding: utf-8

import os

'''
代码仅适用于Python2版本，3版本需要改为range

'''


def file_name_max_len():
    max_len = 0
    try:
        for i in xrange(1, 10**10):
            name = "w" * i
            with open(name, 'w') as ofs:
                ofs.write("test" * 10)
            max_len = i
            os.remove(name)
    except IOError as ioe:
        print("Maximum length of file name is: {}".format(max_len))


def dir_name_max_len():
    max_len = 0
    try:
        name = "w"
        for i in xrange(1, 10**10):
            name = "w" * i
            os.mkdir(name)
            os.rmdir(name)
            max_len = i
    except OSError as ioe:
        print("Maximum length of directory name is: {}".format(max_len))


if __name__ == '__main__':
    file_name_max_len()
    dir_name_max_len()
