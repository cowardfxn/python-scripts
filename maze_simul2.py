#!/usr/bin/python
# encoding: utf-8

from pprint import pprint

def init_maze():
    maze = [[0] * 7 for _ in range(7)]
    walls = [
        (1, 3),
        (2, 1), (2, 5),
        (3, 3), (3, 4),
        (4, 2), #(4, 3),
        (5, 4)
    ]
    for i in range(7):
        maze[i][0] = maze[i][-1] = 1
        maze[0][i] = maze[-1][i] = 1
    for i, j in walls:
        maze[i][j] = 1
    return maze

def path(maze, start, end):
    i, j = start
    ei, ej = end
    stack = [(i, j)]
    while stack:
        i, j = stack[-1]
        if (i, j) == (ei, ej):
            break
        for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            if maze[i + di][j + dj] == 0:
                maze[i + di][j + dj] = 1  # 设置为无法重复已走过的路径，防止在一个位置来回移动
                stack.append((i + di, j + dj))
                break
        else:
            # 没有遇到break时...
            # 上下左右皆不通，退一格
            stack.pop()
    return stack

if __name__ == '__main__':
    maze = init_maze()
    pprint(maze)
    result = path(maze, (1, 1), (5, 5))
    print(result)
