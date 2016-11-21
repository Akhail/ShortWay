#!/usr/bin/python
import evolution
import matplotlib.pyplot as plot
import numpy as np

if __name__ == '__main__':
    
    AG = evolution.ShortWay(populations=80, cities=100)
    
    AG.evolve(count=300, mutation=30, samples=30)
    plot.subplot(1, 2, 1)
    AG.best_way().paint()
    plot.subplot(1, 2, 2)
    AG.wrong_way().paint()
    print(AG.best_way().distance)
    print(AG.wrong_way().distance)
    plot.show()
    # d.evolve(500)
    # best = d.best_way()
    # for x in d.population:
    #     print(x, end=' ')
    # print()
    # best.paint()
    # print(best)
    # plot.show()