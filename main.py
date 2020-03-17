from City import *
from Chromosome import *
from Population import *
import matplotlib.pyplot as plt
import copy

def main():

    current_population = Population.get_random_population(50, 20)
    init_chromosome = current_population.get_fittest_individual()

    best_chromosome = copy.deepcopy(init_chromosome)

    evolution_curve = []

    evolution_curve.append(best_chromosome.get_fitness_value())

    for i in range(500):
        new_population = current_population.evolve_population()
        new_chromosome = new_population.get_fittest_individual()
        evolution_curve.append(new_chromosome.get_fitness_value())
        if new_chromosome < best_chromosome:
            best_chromosome = copy.deepcopy(new_chromosome)

        current_population = new_population
    
    plt.subplot(3, 1, 1)
    chromosome_length = init_chromosome.chromosome_length
    for i in range(chromosome_length):
        current_city = init_chromosome.cities[i % chromosome_length]
        next_city = init_chromosome.cities[(i + 1) % chromosome_length]
        plt.plot([current_city.x, next_city.x], [current_city.y, next_city.y], color='k', marker='o')

    plt.subplot(3, 1, 2)
    for i in range(chromosome_length):
        current_city = best_chromosome.cities[i % chromosome_length]
        next_city = best_chromosome.cities[(i + 1) % chromosome_length]
        plt.plot([current_city.x, next_city.x], [current_city.y, next_city.y], color='r', marker='o')
    
    plt.subplot(3, 1, 3)
    plt.plot(evolution_curve)

    plt.show()

if __name__ == "__main__":
    main()