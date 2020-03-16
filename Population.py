import numpy as np
from Chromosome import *
from GeneticOperators import *
import copy

class Population:

    def __init__(self, population_size: int, chromosome_length: int):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.individuals = []
    
    def __repr__(self):
        res = 'Population(population_size: {})'.format(self.population_size) + '\n'
        for individual in self.individuals:
            res += individual.__repr__() + '\n'
        return res
    
    def evolve_population(self):

        # 1 - calculate fitness value for each chromosome in the population
        for chromosome in self.individuals:
            chromosome.fitness = chromosome.get_fitness_value()
        
        # 2 - sort the chromosomes of the population in ascending order, by their fitness value
        self.individuals = np.sort(self.individuals)

        # 3 - compute sum of fitness values
        fitnesses_values = np.fromiter(map(lambda x: x.fitness, self.individuals), dtype=np.float)

        fitnesses_sum = np.sum(fitnesses_values)

        # 4 - normalize fitnesses by dividing on the total fitness sum
        fitnesses_probabilities = np.divide(fitnesses_values, fitnesses_sum)

        # 5 - construct cumulative sum array
        cumulative_probabilities = np.cumsum(fitnesses_probabilities)

        new_population: Population = Population(self.population_size, self.chromosome_length)

        while len(new_population.individuals) != new_population.population_size:

            first_child_index = GeneticOperators.roulette_wheel_selection(cumulative_probabilities)
            second_child_index = GeneticOperators.roulette_wheel_selection(cumulative_probabilities)

            if first_child_index == second_child_index:
                continue

            first_child = self.individuals[first_child_index]
            second_child = self.individuals[second_child_index]

            offspring = GeneticOperators.order_one_crossover(first_child.cities, second_child.cities)

            # TODO:
            # here, generate a random number, and compare it with the
            # mutation rate, to either mutate the offspring, or not

            mutated_offspring = GeneticOperators.swap_mutation(offspring)
            print(mutated_offspring)

            new_population.individuals.append(mutated_offspring)

        return new_population
    
    @staticmethod
    def get_random_population(population_size, chromosome_length):
        # TODO:
        # the total possible number number of different individuals that can be generated for a `chromosome_length`
        # is factorial of chromosome_length
        # we should make sure that: population_size <= factorial of chromosome_length
        # Also, consider using set or dictionary, so that the population will only contains unique chromosomes
        random_populaton = Population(population_size, chromosome_length)
        random_chromosome = Chromosome.get_random_chromosome(chromosome_length)
        for _ in range(population_size):
            shuffled_chromosome = copy.deepcopy(random_chromosome)
            np.random.shuffle(shuffled_chromosome.cities)
            random_populaton.individuals.append(shuffled_chromosome)
        return random_populaton