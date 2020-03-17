import numpy as np
from Chromosome import *

class GeneticOperators:
    
    # selection operator
    @staticmethod
    def roulette_wheel_selection(cum_prob_arr):
        """
        Roulette Wheel Selection Operator (https://en.wikipedia.org/wiki/Fitness_proportionate_selection)

        This function performs roulette wheel selection to select individual from population

        Parameters:
            cum_prob_arr (numpy array): cumulative probabilities of individuals array
        
        Returns:
            int: index of the selected individual
        """
        random_number = np.random.uniform()
        index = np.searchsorted(cum_prob_arr, random_number)
        return index

    # crossover operator
    @staticmethod
    def order_one_crossover(chromosome_1, chromosome_2):
        chromosome_length = chromosome_1.chromosome_length
        mid = chromosome_length // 2
        start_index = np.random.randint(0, mid + 1)
        end_index = start_index + mid

        offspring_cities = np.ndarray((chromosome_length,), dtype=np.object)

        selected_cities = chromosome_1.cities[start_index:end_index]
        offspring_cities[start_index:end_index] = selected_cities
        copied_cities_ids = set(map(lambda x: x.id, selected_cities))
        to_be_copied_cities_ids = set(map(lambda x: x.id, chromosome_2.cities)) - copied_cities_ids

        chromosome_2_index = (end_index % chromosome_length)
        offspring_index = (end_index % chromosome_length)

        while to_be_copied_cities_ids:

            if chromosome_2.cities[chromosome_2_index].id not in copied_cities_ids:
                offspring_cities[offspring_index] = chromosome_2.cities[chromosome_2_index]
                offspring_index = (offspring_index + 1) % chromosome_length
                to_be_copied_cities_ids.remove(chromosome_2.cities[chromosome_2_index].id)

            chromosome_2_index = (chromosome_2_index + 1) % chromosome_length
        
        offspring_chromosome = Chromosome(chromosome_length)
        offspring_chromosome.cities = offspring_cities
        return offspring_chromosome
    
    # mutation operator
    @staticmethod
    def swap_mutation(chromosome):

        mutated_chromosome_cities = np.copy(chromosome.cities)

        first_index = np.random.randint(0, chromosome.chromosome_length)
        second_index = np.random.randint(0, chromosome.chromosome_length)

        mutated_chromosome_cities[first_index], mutated_chromosome_cities[second_index] = mutated_chromosome_cities[second_index], mutated_chromosome_cities[first_index]
        
        mutated_chromosome = Chromosome(chromosome.chromosome_length)
        mutated_chromosome.cities = mutated_chromosome_cities
        
        return mutated_chromosome