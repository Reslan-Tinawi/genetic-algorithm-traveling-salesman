import numpy as np
from Chromosome import *
from GeneticOperators import *
import copy

class Population:

    def __init__(self, population_size: int, chromosome_length: int, mutation_rate: float):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.individuals = []
        self.mutation_rate = mutation_rate
    
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

        new_population: Population = Population(self.population_size, self.chromosome_length, self.mutation_rate)

        while len(new_population.individuals) != new_population.population_size:

            first_parent_index = GeneticOperators.roulette_wheel_selection(cumulative_probabilities)
            second_parent_index = GeneticOperators.roulette_wheel_selection(cumulative_probabilities)

            if first_parent_index == second_parent_index:
                continue

            first_parent = self.individuals[first_parent_index]
            second_parent = self.individuals[second_parent_index]

            offspring_1 = GeneticOperators.order_one_crossover(first_parent, second_parent)

            offspring_2 = GeneticOperators.order_one_crossover(second_parent, first_parent)
            
            mutated_offspring_1 = GeneticOperators.swap_mutation(offspring_1, self.mutation_rate)
            mutated_offspring_1.get_fitness_value()

            mutated_offspring_2 = GeneticOperators.swap_mutation(offspring_2, self.mutation_rate)
            mutated_offspring_2.get_fitness_value()

            new_population.individuals.append(min(mutated_offspring_1, mutated_offspring_2))
        
        return new_population
    
    def get_fittest_individual(self):
        self.individuals = np.sort(self.individuals)

        return self.individuals[-1]

    @staticmethod
    def get_random_population(population_size, chromosome_length, mutation_rate, chromosome_csv_path):
        # TODO:
        # the total possible number number of different individuals that can be generated for a `chromosome_length`
        # is factorial of chromosome_length
        # we should make sure that: population_size <= factorial of chromosome_length
        # Also, consider using set or dictionary, so that the population will only contains unique chromosomes
        random_populaton = Population(population_size, chromosome_length, mutation_rate)

        if chromosome_csv_path:
            random_chromosome = Chromosome.read_chromosome_from_csv(chromosome_csv_path)
        else:
            random_chromosome = Chromosome.get_random_chromosome(chromosome_length)

        for _ in range(population_size):
            shuffled_chromosome = copy.deepcopy(random_chromosome)
            np.random.shuffle(shuffled_chromosome.cities)
            shuffled_chromosome.get_fitness_value()
            random_populaton.individuals.append(shuffled_chromosome)
        
        random_populaton.individuals = np.sort(random_populaton.individuals)

        return random_populaton
