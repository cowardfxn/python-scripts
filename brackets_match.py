#!/usr/bin/python
# encoding: utf-8

LEFT = ("(", "{", "[")
RIGHT = (")", "}", "]")

def match(expr):
    # 从左向右遍历
    stack = []
    for brackets in expr:
        if brackets in LEFT:
            stack.append(brackets)
        elif brackets in RIGHT:
            # 如果stack为空或遍历到的右括号与已存储的最后一个左括号不匹配，则返回False
            if not stack or not 1 <= ord(brackets) - ord(stack[-1]) <= 2:
                return False
            # 否则判断右括号与已存储的左括号匹配，出栈已匹配到的左括号，继续遍历
            stack.pop()
    return not stack

if __name__ == '__main__':
    print(match("[{}({[]})]"))
