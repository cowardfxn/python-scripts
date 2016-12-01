#!/usr/bin/python
# coding: utf-8

'''
Dive into Python3示例
将英文单词转化为复数形式
'''

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

patterns = (
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('(qu|[^aeiou])y$', 'y$', 'ies'),
    ('$', '$', 's')
)


def rules(patterns):
    for (pattern, search, replace) in patterns:
        yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun):
    for (matches_rule, apply_rule) in rules(patterns):
        if matches_rule(noun):
            return apply_rule(noun)


if __name__ == '__main__':
    print(plural("world"))
