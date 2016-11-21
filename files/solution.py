import copy

import numpy as np


class Solution:
    def __init__(self, cities=None, steps=None):
        """
            :param cities: Specify cities to evaluate
            :param steps: Instance a solution with a solution
        """
        self.steps = None
        
        if steps is None and cities is not None:
            for x in range(len(cities)):
                self.steps = np.random.permutation(cities)
        else:
            self.steps = steps
        
        self.distance = sum([self.steps[i] + self.steps[i - 1] for i in range(1, len(self.steps))])
        
    def __str__(self):
        return str(self.distance)
    
    def __add__(self, other):
        """
            Operator combination
        """
        st = self.steps
        ot = other.steps
        cop = np.copy(st)
        cop[st != ot] = np.random.permutation(cop[st != ot])
        return Solution(steps=cop)
    
    def get_coord(self):
        return [i.x for i in self.steps], [i.y for i in self.steps]
    
    def __mul__(self, other):
        """
            Operator mutation
        """
        cp = copy.copy(self)
        for _ in range(other):
            p = np.random.randint(0, len(cp.steps))
            s = np.random.randint(0, len(cp.steps))
            if p != s:
                aux = cp.steps[p]
                cp.steps[p] = cp.steps[s]
                cp.steps[s] = aux
        cp.distance = sum([cp.steps[i] + cp.steps[i - 1] for i in range(1, len(cp.steps))])
        return cp
    
    def __lt__(self, other):
        return self.distance < other.distance
    
    def __cmp__(self, other):
        return self.distance == other.distance
