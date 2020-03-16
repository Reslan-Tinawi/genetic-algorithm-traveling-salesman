import numpy as np
from Chromosome import *

class GeneticOperators:
    
    # selection operator
    @staticmethod
    def roulette_wheel_selection(cum_prob_arr):
        random_number = np.random.uniform()
        index = np.searchsorted(cum_prob_arr, random_number)
        return index

    # crossover operator
    @staticmethod
    def order_one_crossover(chromosome_1, chromosome_2):
        chromosome_length = chromosome_1.shape[0]
        mid = chromosome_length // 2
        start_index = np.random.randint(0, mid + 1)
        end_index = start_index + mid

        offspring = np.ndarray((chromosome_length,), dtype=np.object)

        sub_array = chromosome_1[start_index:end_index]
        offspring[start_index:end_index] = chromosome_1[start_index:end_index]
        copied_elements = set(map(lambda x: x.id, sub_array))
        to_be_copied_elements = set(map(lambda x: x.id, chromosome_2)) - copied_elements

        chromosome_2_index = end_index
        offspring_index = end_index

        while to_be_copied_elements:
            
            if chromosome_2[chromosome_2_index].id not in copied_elements:
                offspring[offspring_index] = chromosome_2[chromosome_2_index]
                offspring_index = (offspring_index + 1) % chromosome_length
                to_be_copied_elements.remove(chromosome_2[chromosome_2_index].id)

            chromosome_2_index = (chromosome_2_index + 1) % chromosome_length

        offspring_chromosome = Chromosome(chromosome_length)
        offspring_chromosome.cities = offspring
        return offspring_chromosome
    
    # mutation operator
    @staticmethod
    def swap_mutation(chromosome):
        mutated_chromosome = np.copy(chromosome)
        chromosome_length = chromosome.shape[0]
        first_index = np.random.randint(0, chromosome_length)
        second_index = np.random.randint(0, chromosome_length)

        mutated_chromosome[first_index], mutated_chromosome[second_index] = mutated_chromosome[second_index], mutated_chromosome[first_index]
        
        return mutated_chromosome