import numpy as np
from City import *
import matplotlib.pyplot as plt

class Chromosome:

    def __init__(self, chromosome_length: int):
        self.chromosome_length = chromosome_length
        # TODO:
        #   what should be the value of cities initially
        self.cities = []
        self.fitness = None
    
    def __repr__(self):
        res = 'Chromosome(chromosome_length: {})'.format(self.chromosome_length) + '\n'
        for city in self.cities:
            res += city.__repr__() + '\n'
        res += 'fitness value: {}'.format(self.fitness)
        return res
    
    def __lt__(self, other_chromosome):
        return self.fitness < other_chromosome.fitness
    
    def plot_solution(self):
        x_s = np.fromiter(map(lambda city: city.x, self.cities), dtype=np.float)
        y_s = np.fromiter(map(lambda city: city.y, self.cities), dtype=np.float)
        plt.scatter(x_s, y_s)
        plt.show()
    
    def get_fitness_value(self):
        self.fitness = 0
        for i in range(self.chromosome_length):
            current_city = self.cities[i % self.chromosome_length]
            next_city = self.cities[(i + 1) % self.chromosome_length]
            self.fitness += current_city.distance_to(next_city)
        
        return self.fitness

    @staticmethod
    def get_random_chromosome(chromosome_length: int):
        random_chromosome = Chromosome(chromosome_length)
        # TODO
        #   find a better way to initialize the cities array
        random_chromosome.cities = np.array([City.get_random_city() for _ in range(chromosome_length)])
        for i in range(chromosome_length):
            random_chromosome.cities[i].id = i
        return random_chromosome