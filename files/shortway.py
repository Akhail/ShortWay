import numpy as np

from ShortWay.files.city import City
from ShortWay.files.solution import Solution


class ShortWay:
    def __init__(self, populations=10, cities=None):
        if isinstance(cities, int):
            self.cities = [City() for _ in range(cities)]  # Generate the cities
        elif cities is None:
            self.cities = [City() for _ in range(10)]  # Generate the cities
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
    
    def evolve(self, count=1, mutation=.3, samples=.3):
        quantity = int(len(self.population) * samples)
        for _ in range(count):
            samples = self.population[:quantity]  # Choice the parents
            before = None
            for i in range(len(samples)):
                solution = np.random.choice(samples)
                if i != 0:
                    sol = solution + before  # Combination
                    if np.random.rand() <= mutation:
                        sol *= np.random.randint(1, 4)  # Mutation
                    idx = np.searchsorted(self.population, sol)  # Find the index what maintain the order
                    self.population = np.insert(self.population, idx, sol)
                before = solution
    
            self.population = self.population[:self.quantity]
