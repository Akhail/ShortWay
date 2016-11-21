#!/usr/bin/python
import matplotlib.pyplot as plt

from ShortWay.files.shortway import ShortWay

if __name__ == '__main__':
    
    AG1 = ShortWay(populations=80, cities=100)
    # AG2 = ShortWay(populations=60, cities=20)
    plt.ion()
    ant = AG1.best_way().distance
    for _ in range(10000):
        AG1.evolve()
        sol1 = AG1.best_way()
        if ant != sol1.distance:
            plt.clf()
            x, y = sol1.get_coord()
            ant = sol1.distance
            plt.plot(x, y)
            plt.plot(x, y, 'ro')
            print(sol1.distance)
            plt.pause(.1)
    print('Fin')
    plt.pause(10)
    