"""
Input class makes all the work
related to Npuzzle input
"""

import logging
import sys

class Input:

    def __init__(self, filename=None):
        if not filename:
            print('No filename entered')
            sys.exit(1)
        self.filename = filename

    def get_content(self):
        with open(self.filename, 'r') as f:
            content = f.readlines()
        return content

if __name__ == '__main__':
    i = Input('map.np')
    print(i.get_content())
