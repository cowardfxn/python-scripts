#!/usr/bin/python
# encoding: utf-8

'''
Python的类继承链MRO
原理验证

'''

class A(object):
    def __init__(self):
        print '    -> Enter A'
        print '    <- Leave A'

class B(A):
    def __init(self):
        print '    -> Enter B'
        # A.__init__(self)
        super(B, self).__init__()
        print '    <- Leave B'

class C(A):
    def __init__(self):
        print "    -> Enter C"
        # A.__init__(self)
        super(C, self).__init__()
        print "    <- Leave C"

class D(B, C):
    def __init__(self):
        print "    -> Enter D"
        # B.__init__(self)
        # C.__init__(self)
        super(D, self).__init__()
        print "    <- Leave D"

if __name__ == "__main__":
    d = D()
    print "MRO:", [x.__name__ for x in D.__mro__]
    print type(D.__mro__)
