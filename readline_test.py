#!/usr/bin/python
# _*_ encoding: utf-8 _*_

"""
读取空行会读到换行符，即使没有输出，布尔值也不是False

"""
fs.seek(0)
l=fs.next()
while l:
    print "line:", l
    print "bool(line):", bool(l)
    print "---"*3
    l=fs.next()

fs.seek(0)
l=fs.readline()
while l:
    print "line:", l
    print "bool(line):", bool(l)
    print "---"*3
    l=fs.readline()
