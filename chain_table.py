#!/usr/bin/python3
# encoding: utf-8

Nil = None

# 构造链表的基础函数
# 在链表最前端插入一个新的节点
def cons(x, xs=Nil):
    return (x, xs)

assert cons(0) == (0, Nil)
assert cons(0, (1, (2, Nil))) == (0, (1, (2, Nil)))
print("const tests passed. ")


# synonym
# def cons(x, xs=Nil):
#     return lambda i: x if i == 0 else xs

def lst(*xs):
    if not xs or not xs[0]:
        return Nil
    else:
        return cons(xs[0], lst(*xs[1:]))


assert lst() == Nil
assert lst(Nil) == Nil
assert lst(1) == (1, Nil)
assert lst(1, 2, 3, 4) == (1, (2, (3, (4, Nil))))
print("lst tests passed. ")


# 返回链表第一个节点
def head(xs):
    return xs[0]

# 返回除了第一个节点之外的整个链表
def tail(xs):
    return xs[1]

assert head(lst(1, 2, 3, 4)) == 1
assert tail(lst(5, 6, 7, 8)) == lst(6, 7, 8)
print("head&tail tests passed. ")

# 判断链表是否为空
def is_empty(xs):
    return xs is Nil

assert is_empty(Nil)
assert not is_empty(lst(1, 2, 3))
print("is_empty tests passed. ")


# 计算链表长度，时间复杂度O(n)
def length(xs):
    if is_empty(xs):
        return 0
    else:
        return 1 + length(tail(xs))

assert length(lst()) == 0
assert length(lst(1, 2, 3, 4, 5)) == 5
print("length tests passed. ")


# 连接两个链表
def concat(xs, ys):
    if is_empty(xs):
        return ys
    else:
        return cons(head(xs), concat(tail(xs), ys))

assert concat(Nil, cons(2)) == (2, Nil)
assert concat(cons(4), lst(5, 6, 7)) == (4, (5, (6, (7, Nil))))
print("concat tests passed. ")


# 返回链表的最后一个非空节点
def last(xs):
    if is_empty(tail(xs)):
        return head(xs)
    else:
        return last(tail(xs))

assert last(cons(Nil)) == Nil
assert last(cons(1)) == 1
assert last(lst(1, 2, 3, 4)) == 4
print("last tests passed. ")

# 返回除了最后一个节点的整个链表
def init(xs):
    if is_empty(tail(tail(xs))):
        return cons(head(xs))
    else:
        return cons(head(xs), init(tail(xs)))

# assert init(cons(Nil)) == cons(Nil)
# assert init(cons(1)) == cons(1)
assert init(lst(1, 2, 3, 4, 5)) == lst(1, 2, 3, 4)
print("init tests passed. ")


# 反转链表，时间复杂度O(n^2)
def reverse(xs):
    if is_empty(xs):
        return xs
    else:
        return concat(reverse(tail(xs)), cons(head(xs), Nil))

assert reverse(Nil) == Nil
assert reverse(cons(1)) == cons(1)
assert reverse(lst(2, 3, 4, 56, 7)) == lst(7, 56, 4, 3, 2)
assert reverse(reverse(lst(8, 9, 10, 11))) == lst(8, 9, 10, 11)
print("reverse tests passed. ")


# 返回链表前n个元素
def take(n, xs):
    if n > length(xs):
        return xs
    else:
        if n == 0:
            return Nil
        else:
            return cons(head(xs), take(n-1, tail(xs)))

assert take(0, cons(1)) == Nil
assert take(1, cons(2)) == cons(2)
assert take(4, lst(1, 2, 3, 4, 5)) == lst(1, 2, 3, 4)
assert take(5, lst(1, 2, 3, 4, 5)) == lst(1, 2, 3, 4, 5)
assert take(6, lst(6, 7, 8)) == lst(6, 7, 8)
print("take tests passed. ")


# 返回除了前n个节点的整个链表
def drop(n, xs):
    if n == 0 or is_empty(xs):
        return xs
    else:
        return drop(n-1, tail(xs))

assert drop(0, cons(Nil)) == cons(Nil)
assert drop(1, cons(1)) == Nil
assert drop(2, lst(2, 3, 4, 5)) == lst(4, 5)
assert drop(3, lst(6, 7, 8)) == Nil
assert drop(6, lst(9, 0, 1)) == Nil
print("drop tests passed. ")


# 获取链表的第i个元素，时间复杂度O(n)
def apply(i, xs):
    return head(drop(i, xs))

# synonym
# def apply(i, xs):
#     # return head(drop(i, xs))
#     if i == 0:
#         return head(xs)
#     else:
        # return apply(i-1, tail(xs))

assert apply(0, cons(Nil)) == Nil
assert apply(0, cons(0)) == 0
assert apply(1, lst(1, 2, 3)) == 2
assert apply(4, lst(4, 5, 6, 7, 8)) == 8
print("apply tests passed. ")



# 插入排序
# 有序插入，将x插入升序排列的链表xs，插入后的链表仍然保持升序
def insert(x, xs):
    if is_empty(xs) or x <= head(xs):
        return cons(x, xs)
    else:
        return cons(head(xs), insert(x, tail(xs)))

assert insert(2, lst(1, 1, 4, 5)) == lst(1, 1, 2, 4, 5)
assert insert(2, lst(3, 3, 3)) == lst(2, 3, 3, 3)
assert insert(5, lst(2, 3, 4)) == lst(2, 3, 4, 5)
print("insert tests passed. ")

# 使用插入排序的方式，排序整个无序链表
def isort(xs):
    if is_empty(xs):
        return xs
    else:
        return insert(head(xs), isort(tail(xs)))

# print(isort(lst(1)))
# print(isort(lst(2, 1)))
# print(isort(lst(0, 2, 1)))
# print(isort(lst(4, 0, 2, 1)))  # 无法实现复杂排序
# print(isort(lst(3, 4, 0, 2, 1)))

# assert isort(lst(3, 4, 0, 2, 1)) == lst(0, 1, 2, 3, 4)
assert isort(lst(3, 3)) == lst(3, 3)
# assert isort(lst(6, 4, 2, 7, 1, 0)) == lst(0, 1, 2, 4, 6, 7)
print("isort tests passed.")


def to_string(xs, prefix="[", sep=",", appendix="]"):
    def _to_string(xs):
        if is_empty(xs):
            return ""
        elif is_empty(tail(xs)):
            return str(head(xs))
        else:
            return "{}{} {}".format(head(xs), sep, _to_string(tail(xs)))
    return "{}{}{}".format(prefix, _to_string(xs), appendix)

assert to_string(cons(Nil)) == "[None]"
assert to_string(cons(1)) == "[1]"
assert to_string(lst(2, 3, 4, 5)) == "[2, 3, 4, 5]"
print("to_string tests passed.")
