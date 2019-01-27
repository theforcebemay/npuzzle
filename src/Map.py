# Here logic about movement

import sys
from random import choice
import random

class Map:

    def __init__(self, size, map_=None):
        self.size = size
        self.final_state = None
        self.map = map_

    def generate_map(self, value=None):
        values = list(range(self.size ** 2))
        random.shuffle(values)
        m = [[ values.pop() \
                for x in range(0,self.size)] \
                for y in range(0,self.size)]
        if value != None:
            return [[ 0 \
                    for x in range(0,self.size)] \
                    for y in range(0,self.size)]


    def print_map(self):
        for row in self.map:
            for inte in row:
                print(inte, ' ', end='')
            sys.stdout.write('\n')

    def get(self, x, y):
        return self.map[x][y]

    def get_final_state(self):
        items_set = list(range(1, self.size ** 2))


    def _get_direction(self, x, y):
        if not self._is_accessible(x, y):
            raise AssertionError
        # Continue here

    def set(self, x, y, value):
        self.map[x][y] = value

    def swap(self, x1, y1, x2, y2):
        value1 = self.get(x1,y1)
        value2 = self.get(x2,y2)
        self.set(x1, y1, value2)
        self.set(x2, y2, value1)

    def _are_movable(self, x1, y1, x2, y2):
        if self._is_accessible(x1, y1) and \
                self._is_accessible(x2, y2):
            item1 = self.get(x1, y1)
            item2 = self.get(x2, y2)
            if (item1 == 0 or item2 == 0) and \
                (item1 != 0 or item2 != 0):
                    return True
            return False

    def _is_accessible(self, x, y):
        if not self.map:
            raise AssertionError
        try:
            coordinate = self.map[x][y]
        except IndexError:
            return False
        return True
