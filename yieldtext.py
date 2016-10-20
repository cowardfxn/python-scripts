#!/env/python
# encoding: utf-8

'''
测试yield函数
不能与return出现在同一个函数中
'''

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a+b
        n += 1
        print 'a', a
        # yield b
        print n

if __name__ == '__main__':
    fab(7)
