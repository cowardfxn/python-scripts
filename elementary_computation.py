#!/usr/bin/python
# encoding: utf-8

operators = {
    "+": lambda op1, op2: op1 + op2,
    "-": lambda op1, op2: op1 - op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2,
}

def eval_posix(e):
    # 从左向右读取操作数
    # 从右向左应用操作符
    # 不考虑运算符优先级
    tokens = e.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            f = operators[token]
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f(op1, op2))
    return stack.pop()

if __name__ == '__main__':
    print(eval_posix("2 3 4 * +"))
    print(eval_posix("1 2 3 4 + - *"))
