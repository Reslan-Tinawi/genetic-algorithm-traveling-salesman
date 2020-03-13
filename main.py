from City import *
from Chromosome import *
from Population import *
import matplotlib.pyplot as plt


def main():
    init_population = Population.get_random_population(4, 2)

    for chromosome in init_population.individuals:
        chromosome.get_fitness_value()
    
    init_population.individuals = np.sort(init_population.individuals)
    fitnesses_values = np.fromiter(map(lambda x: x.fitness, init_population.individuals), dtype=np.float)
    print(fitnesses_values)


if __name__ == "__main__":
    main()