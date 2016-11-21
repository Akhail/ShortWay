import numpy as np
import matplotlib.pyplot as plot
import copy


class Solution:
    def __init__(self, cities=None, steps=None):
        self.steps = None
        if steps is None and cities is not None:
            for x in range(len(cities)):
                self.steps = np.random.permutation(cities)
        else:
            self.steps = steps
        
        self.distance = sum([self.steps[i] + self.steps[i-1] for i in range(1, len(self.steps))])
            
    def __str__(self):
        return str(self.distance)
    
    def __add__(self, other):
        st = self.steps
        ot = other.steps
        cop = np.copy(st)
        cop[st != ot] = np.random.permutation(cop[st != ot])
        return Solution(steps=cop)
    
    def __mul__(self, other):
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
    
    def paint(self):
        x = [x.x for x in self.steps]
        y = [y.y for y in self.steps]
        plot.plot(x, y, 'ro')
        plot.plot(x, y)
        
    def __lt__(self, other):
        return self.distance < other.distance
        
    def __cmp__(self, other):
        return self.distance == other.distance
     
        
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
        x = self.x - other.x
        y = self.y - other.y
        return np.hypot(x, y)
        
        
class ShortWay:
    def __init__(self, populations=10, cities=None):
        
        if isinstance(cities, int):
            self.cities = [City() for _ in range(cities)]           # Genera las ciudades
        elif cities is None:
            self.cities = [City() for _ in range(10)]  # Genera las ciudades
        else:
            self.cities = cities
            
        self.quantity = populations
        self.population = np.array([Solution(self.cities) for _ in range(populations)])
        self.population = np.sort(self.population)
    
    def reset_population(self):
        self.population = np.array([Solution(self.cities) for _ in range(self.quantity)])
        self.population = np.sort(self.population)
    
    def best_way(self):
        return self.population[0]
    
    def wrong_way(self):
        return self.population[-1]
    
    def evolve(self, count=10, mutation=30, samples=30):
        for _ in range(count):
            self._evolute(mutation, samples)
    
    def _evolute(self,  mutation, samples):
        quantity = int(len(self.population) * samples / 100)
        samples = self.population[:quantity]
        
        before = None
        for i in range(len(samples)):
            solution = np.random.choice(samples)
            if i != 0:
                sol = solution + before                         # Emparejamiento
                if np.random.randint(0, 100) < mutation:
                    sol *= np.random.randint(1, 4)  # Mutacion
                idx = np.searchsorted(self.population, sol)
                self.population = np.insert(self.population, idx, sol)
            before = solution

        self.population = self.population[:self.quantity]