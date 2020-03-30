import numpy as np
from City import *
import pandas as pd

class Chromosome:

    def __init__(self, chromosome_length: int):
        self.chromosome_length = chromosome_length
        # TODO:
        #   what should be the value of cities initially
        self.cities = []
        self.fitness: float = None
    
    def __repr__(self):
        res = 'Chromosome(chromosome_length: {})'.format(self.chromosome_length) + '\n'
        for city in self.cities:
            res += city.__repr__() + '\n'
        res += 'fitness value: {}'.format(self.fitness)
        return res
    
    def __lt__(self, other_chromosome: 'Chromosome'):
        return self.fitness < other_chromosome.fitness
    
    def get_fitness_value(self):
        if self.fitness == None:
            self.fitness = 0
            for i in range(self.chromosome_length):
                current_city = self.cities[i % self.chromosome_length]
                next_city = self.cities[(i + 1) % self.chromosome_length]
                self.fitness += current_city.distance_to(next_city)
            self.fitness = 1 / (self.fitness + 1)
        return self.fitness

    def get_cities_ids(self):
        cities_ids = np.fromiter(map(lambda city: city.id, self.cities), dtype=np.int)
        return cities_ids
    
    def get_cities_coordinates(self):
        x_s_coordinates = np.fromiter(map(lambda city: city.x, self.cities), dtype=np.float)
        y_s_coordinates = np.fromiter(map(lambda city: city.y, self.cities), dtype=np.float)
        return x_s_coordinates, y_s_coordinates

    @staticmethod
    def get_random_chromosome(chromosome_length: int):
        random_chromosome = Chromosome(chromosome_length)
        # TODO
        #   find a better way to initialize the cities array
        random_chromosome.cities = np.array([City.get_random_city() for _ in range(chromosome_length)])
        for i in range(chromosome_length):
            random_chromosome.cities[i].id = i
        return random_chromosome
    
    @staticmethod
    def read_chromosome_from_csv(csv_path):
        data = pd.read_csv(csv_path)
        
        ids = data['ids'].values
        x_s = data['x'].values
        y_s = data['y'].values

        chromosome_length = len(ids)
        chromosome = Chromosome(chromosome_length)
        chromosome.cities = np.array([City(x_s[i], y_s[i], ids[i]) for i in range(chromosome_length)])

        return chromosome
