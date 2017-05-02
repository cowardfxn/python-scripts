#!/usr/bin/python
# encoding: utf-8

def knapstack(t, w):
    """
    :param t: 背包总容量
    :param w: 物品重量列表
    :return:
    """
    n = len(w)
    stack = []
    k = 0
    while stack or k < n:
        while t > 0 and k < n:
            if t >= w[k]:
                stack.append(k)
                t -= w[k]
            k += 1
        if t == 0:  # 如果刚好装满...
            print(stack)
        k = stack.pop()  # 最后一个元素已经测试完毕，恢复k，尝试其他组合
        t += w[k]
        k += 1

if __name__ == '__main__':
    print(knapstack(10, [1, 8, 4, 3, 5, 2]))
