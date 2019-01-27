
# Guard validates input
# Comments, number of digits, etc.

from Input import Input
from Map import Map
import sys

class Line:

    def __init__(self, line):
        self.elements = line.split()
        self.len = len(self.elements)
        self.only_ints = False
        if self.len:
            self.only_ints = all([element.isdigit() for element in self.elements])
        if not self.only_ints and self.len > 0:
            raise AssertionError('Not integer in map?')

    def is_empty(self):
        return not self.len

    def is_map_size(self):
        return self.len == 1 and self.only_ints

    def get_value(self):
        return int(self.elements[0])

class Guard:

    def __init__(self, nmap):
        self.map = [line.split('#')[0] for line in nmap]
        self.mapsize = None
        self.fine_map = []

    def print_map(self):
        for line in self.map:
            print(line)

    @staticmethod
    def are_unique(digits):
        adigits = len(digits)
        bdigits = len(list(set(digits)))
        return adigits == bdigits

    def read_map(self):
        self.items = []
        for line in self.map:
            l = Line(line)
            if l.is_map_size():
                if self.mapsize:
                    raise AssertionError('Two mapsizes? ')
                self.mapsize = l.get_value()
            elif l.is_empty():
                pass
            else:
                if not l.len == self.mapsize:
                    raise AssertionError('Wrong mapsize?')
                self.items.extend(l.elements)
                self.fine_map.append(l.elements)
        if not self.are_unique(self.items):
        	sys.exit()

    @property
    def get_map(self):
    	if self.fine_map:
    		return self.fine_map, self.mapsize
