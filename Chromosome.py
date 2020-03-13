import numpy as np
from City import *

class Chromosome:

    def __init__(self, chromosome_length: int):
        self.chromosome_length = chromosome_length
        # TODO:
        #   what should be the value of cities initially
        self.cities: List[City] = []
        self.fitness = 0.0
    
    def __repr__(self):
        res = 'Chromosome(chromosome_length: {})'.format(self.chromosome_length) + '\n'
        for city in self.cities:
            res += city.__repr__() + '\n'
        res += 'fitness value: {}'.format(self.fitness)
        return res
    
    def __lt__(self, other_chromosome: 'Chromosome') -> bool:
        return self.fitness < other_chromosome.fitness
        pass
    
    def plot_solution(self):
        x_s = np.fromiter(map(lambda city: city.x, self.cities), dtype=np.float)
        y_s = np.fromiter(map(lambda city: city.y, self.cities), dtype=np.float)
        return x_s, y_s
    
    def get_fitness_value(self) -> float:
        fitness_value = 0.0
        for i in range(self.chromosome_length):
            current_city = self.cities[i% self.chromosome_length]
            next_city = self.cities[(i + 1) % self.chromosome_length]
            fitness_value += current_city.distance_to(next_city)
        self.fitness = fitness_value
        return fitness_value

    @staticmethod
    def get_random_chromosome(chromosome_length: int) -> 'Chromosome':
        random_chromosome = Chromosome(chromosome_length)
        # TODO
        #   find a better way to initialize the cities array
        random_chromosome.cities = np.array([City.get_random_city() for _ in range(chromosome_length)])
        return random_chromosome