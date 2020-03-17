from Population import *

class GeneticAlgorithm:
    
    def __init__(self, number_of_iterations, population_size, chromosome_length, mutation_rate, chromosome_csv_path=None):
        self.number_of_iterations = number_of_iterations
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.initial_chromosome = None
        self.best_chromosome = None
        self.evolution_curve = []
        self.chromosome_csv_path = chromosome_csv_path

    def solve(self):

        current_population = Population.get_random_population(self.population_size, self.chromosome_length, self.mutation_rate, self.chromosome_csv_path)
        self.init_chromosome = current_population.get_fittest_individual()

        self.best_chromosome = copy.deepcopy(self.init_chromosome)

        self.evolution_curve = []

        self.evolution_curve.append(self.best_chromosome.get_fitness_value())

        for i in range(self.number_of_iterations):
            new_population = current_population.evolve_population()
            new_chromosome = new_population.get_fittest_individual()
            
            if new_chromosome < self.best_chromosome:
                self.best_chromosome = copy.deepcopy(new_chromosome)

            self.evolution_curve.append(self.best_chromosome.get_fitness_value())

            current_population = new_population
        
    def plot(self):
        plt.subplot(3, 1, 1)
        for i in range(self.chromosome_length):
            current_city = self.init_chromosome.cities[i % self.chromosome_length]
            next_city = self.init_chromosome.cities[(i + 1) % self.chromosome_length]
            plt.plot([current_city.x, next_city.x], [current_city.y, next_city.y], color='k', marker='o')

        plt.subplot(3, 1, 2)
        for i in range(self.chromosome_length):
            current_city = self.best_chromosome.cities[i % self.chromosome_length]
            next_city = self.best_chromosome.cities[(i + 1) % self.chromosome_length]
            plt.plot([current_city.x, next_city.x], [current_city.y, next_city.y], color='r', marker='o')
        
        plt.subplot(3, 1, 3)
        plt.plot(self.evolution_curve)

        plt.show()