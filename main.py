from City import *
from Chromosome import *
from Population import *
import matplotlib.pyplot as plt


def main():
    # init_population = Population.get_random_population(4, 2)
    # new_population = init_population.evolve_population()
    chromosome_1 = Chromosome.get_random_chromosome(6)
    chromosome_2 = Chromosome.get_random_chromosome(6)
    print(chromosome_1)
    print(chromosome_2)

if __name__ == "__main__":
    main()