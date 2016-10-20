#!/user/bin/python
# _*_ encoding: utf-8 _*_

'''
单例模式试验
两种实现方式

'''

class A(object):
    _dict = {}
    def __new__(cls):
        if 'key' in A._dict:
            print 'Exists'
            return A._dict['key']
        else:
            print 'New'
            return super(A, cls).__new__(cls)
    def __init__(self):
        print "Init"
        A._dict['key'] = self
        print ''

class C(object):
    _t = None
    def __new__(cls):
        if not C._t:
            C._t = lambda x: x*4
        return C._t
    def __init__(self):
        C._t = lambda x: x*4


class B(object):
    @staticmethod
    def static(a, b):
        print "static"
        print a
        print b

    def norm_funct(self, a, b):
        print "norm"
        print a
        print b

    @classmethod
    def cls_func(cls, a, b):
        print "cls_func"
        print cls.static("inner", 'cls=>static')
        print a
        print b

if __name__ == "__main__":
    a1 = A()
    a2 = A()
    a3 = A()

    b = B()
    b.static(1, 2)
    b.cls_func(3, 4)
    b.norm_funct(5, 6)
    B.static(7, 8)
    B.norm_funct(9, 10)
    B.cls_func(11, 12)

