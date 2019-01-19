
# Guard validates input
# Comments, number of digits, etc.

from Input import Input

class Guard:

    def __init__(self, nmap):
        self.map = nmap
        self.mapsize = None
        self._delete_comments()

    def _delete_comments(self):
        self.map = [line.split('#')[0] for line in self.map]

    def print_map(self):
        for line in self.map:
            print(line, end="")

    def get_mapsize(self):
        pass
