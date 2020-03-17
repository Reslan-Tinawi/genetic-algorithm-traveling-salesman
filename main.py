from City import *
from Chromosome import *
from Population import *
import matplotlib.pyplot as plt
import copy

def main():

    current_population = Population.get_random_population(50, 12)
    init_chromosome = current_population.get_fittest_individual()

    best_chromosome = copy.deepcopy(init_chromosome)

    for i in range(100):
        new_population = current_population.evolve_population()
        new_chromosome = new_population.get_fittest_individual()

        if new_chromosome < best_chromosome:
            best_chromosome = copy.deepcopy(new_chromosome)

        current_population = new_population

if __name__ == "__main__":
    main()