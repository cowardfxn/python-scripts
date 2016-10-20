#!/usr/bin/pyton
# _*_ encoding: utf-8 _*_

"""
Hofstadter Q序列

Q(n)=Q(n-Q(n-1))+Q(n−Q(n−2))

新式类/旧式类 统一type和__class__的返回结果
"""
class qsequence(object):
    def __init__(self, s):
        self.s = s[:]

    def next(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def  current_state(self):
        return self.s

if __name__ == '__main__':
    Q = qsequence([1, 2])
    print next(Q)
    print next(Q)
    print [next(Q) for __ in xrange(10)]
