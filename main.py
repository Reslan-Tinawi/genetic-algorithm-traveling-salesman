from City import *
from Chromosome import *
from Population import *
import matplotlib.pyplot as plt


def main():
    init_population = Population.get_random_population(2, 5)
    new_population = init_population.evolve_population()

if __name__ == "__main__":
    main()