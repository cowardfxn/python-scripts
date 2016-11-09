#!/usr/bin/python
# encoding: utf-8

import UserList

class ChainedList(UserList.UserList):
     def __init__(self, initlist=None):
          self.prv_idx = 0
          super(ChainedList, self).__init__(initlist)
     def __getitem__(self, i):
          self.prv_idx = self.prv_idx < self.__len__() and self.prv_idx or 0
          val = super(ChainedList, self).__getitem__(self.prv_idx)
          self.prv_idx += 1
          return val


def print_heart(word):
     lenth = len(word)
     word = ChainedList(word)
     a = 0.05
     b = 0.11
     c1 = '\n'.join([''.join([(word[(x-y)%lenth] if ((x*a)**2+(y*b)**2-1)**3-(x*a)**2*(y*b)**3<=0 else ' ') for x in range(-40,40)]) for y in range(15,-15,-1)])
     all_str = ''.join(['\033[1;31;40m', c1, '\033[0m'])
     print(all_str)

if __name__ == '__main__':
     # Change the sentence as you wish.
     print_heart("Show me the money!")
