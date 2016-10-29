#!/usr/bin/python
# encoding: utf-8

from random import choice
from pprint import pprint

'''
默认左上角为坐标原点，不允许原地不动，允许走回头路
printTrace列出所有经过的点
'''

class Maze(object):
    def __init__(self, maze_width, maze_height, step_size=1, init_pos=(0, 0)):
        self.pos = list(init_pos)
        self.trace = [list(init_pos)]
        self.width = maze_width
        self.height = maze_height
        self.step = step_size
        self.movements = [1, -1]
        self.movements = [e * self.step for e in [1, -1]]
    def move(self):
        if self.completed():
            raise Exception("You're now out of the maze!")
        else:
            direction = choice(range(len(self.pos)))
            movement = choice(self.movements)
            self.pos[direction] += movement
            self.trace.append(list(self.pos))
        return self.pos
    def completed(self):
        if abs(self.pos[0]) == self.height - 1 or self.pos[0] == 0 or abs(self.pos[1]) == self.width - 1 or self.pos[1] == 0:
            return True
        else:
            return False
    def getTrace(self):
        return self.trace
    def printTrace(self):
        trace_graph = []
        for e in range(self.height):
            trace_graph.append(list("." * self.width))
        for cnt, (r, c) in enumerate(self.trace):
            # trace_graph[r][c] = "%02d" % (cnt + 1)
            trace_graph[r][c] = "O"
        pprint(trace_graph)
    def reset(self):
        self.pos = [choice(range(self.height)), choice(range(self.width))]
        self.trace = [list(self.pos)]

def run(maze):
    while 1:
        try:
            maze.move()
        except Exception as e:
            break
    try:
        maze.printTrace()
    except Exception as e:
        print maze.trace

if __name__ == '__main__':
    for i in range(1000):
        g1 = Maze(4, 4, init_pos=(1,2))
        run(g1)
