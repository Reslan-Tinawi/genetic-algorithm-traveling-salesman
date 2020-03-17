from City import *
from Chromosome import *
from Population import *
from GeneticAlgorithm import *
import matplotlib.pyplot as plt
import copy

def main():

    ga = GeneticAlgorithm(100, 100, 12, 0.3, 'data/data 20 (circle).csv')
    ga.solve()
    ga.plot()


if __name__ == "__main__":
    main()