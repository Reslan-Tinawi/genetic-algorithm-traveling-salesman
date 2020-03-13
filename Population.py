import numpy as np
from Chromosome import *
import copy

class Population:

    def __init__(self, population_size: int, chromosome_length: int):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.individuals: List['Chromosome'] = []
    
    def __repr__(self):
        res = 'Population(population_size: {})'.format(self.population_size) + '\n'
        for individual in self.individuals:
            res += individual.__repr__() + '\n'
        return res
    
    def evolve_population(self) -> 'Population':
        new_population: Population = copy.deepcopy(self)
        # 1 - calculate fitness value for each chromosome in the population

        for chromosome in new_population.individuals:
            chromosome.fitness = chromosome.get_fitness_value()
        
        # 2 - sort the chromosomes of the population in ascending order, by their fitness value
        new_population.individuals = np.sort(new_population.individuals)

        # 3 - compute sum of fitness values
        fitnesses_values = np.fromiter(map(lambda x: x.fitness), new_population.individuals)

        fitnesses_sum = np.sum(new_population.individuals)

        # 4 - normalize fitnesses by dividing on the total fitness sum
        fitnesses_probabilities = np.divide(fitnesses_values, fitnesses_sum)

        # 5 - construct cumulative sum array
        cumulative_probabilities = np.cumsum(fitnesses_probabilities)

        for _ in range(self.population_size):

            first_child = []
            second_child = []
        
        return new_population
    
    @staticmethod
    def get_random_population(population_size, chromosome_length) -> 'Population':
        random_populaton = Population(population_size, chromosome_length)
        random_populaton.individuals = np.array([Chromosome.get_random_chromosome(chromosome_length) for _ in range(population_size)])
        return random_populaton