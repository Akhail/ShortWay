import numpy as np


class City:
    def __init__(self):
        self.x = np.random.randint(-80, 80, dtype=int)
        self.y = np.random.randint(-80, 80, dtype=int)
    
    def __cmp__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __str__(self):
        return "(%i, %i)" % (self.x, self.y)
    
    def __add__(self, other):
        """
            Distance euclidean between two cities
        """
        x = self.x - other.x
        y = self.y - other.y
        return np.hypot(x, y)
