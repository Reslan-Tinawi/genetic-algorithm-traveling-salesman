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
        offspring_cities = np.ndarray((chromosome_length,), dtype=np.object)

        start_pos, end_pos = 0, 0
        copied_cities_ids = set()
        offspring_index = 0

        while True:
            random_1, random_2 = np.random.randint(low=0, high=chromosome_length, size=(2,))
            start_pos = min(random_1, random_2)
            end_pos = max(random_1, random_2)

            if start_pos != end_pos:
                break
        
        selected_cities = chromosome_1.cities[start_pos:end_pos]
        offspring_cities[start_pos:end_pos] = selected_cities
        copied_cities_ids = set([city.id for city in selected_cities])
        offspring_none_indices = np.where(offspring_cities==None)[0]

        for city in chromosome_2.cities:
            if city.id not in copied_cities_ids:
                offspring_element_index = offspring_none_indices[offspring_index]
                offspring_cities[offspring_element_index] = city
                offspring_index += 1
        
        offspring_chromosome = Chromosome(chromosome_length)
        offspring_chromosome.cities = offspring_cities

        return offspring_chromosome
    
    # mutation operator
    @staticmethod
    def swap_mutation(chromosome, mutation_rate):
        mutated_chromosome_cities = np.copy(chromosome.cities)
        chromosome_length = chromosome.chromosome_length

        for i in range(chromosome_length):
            random_number = np.random.random()

            if random_number < mutation_rate:
                j = i
                while j != i:
                    j = np.random.randint(0, chromosome_length)
                mutated_chromosome_cities[i], mutated_chromosome_cities[j] = mutated_chromosome_cities[j], mutated_chromosome_cities[i]

        mutated_chromosome = Chromosome(chromosome_length)
        mutated_chromosome.cities = mutated_chromosome_cities

        return mutated_chromosome