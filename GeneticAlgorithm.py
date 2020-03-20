from Population import *

class GeneticAlgorithm:
    
    def __init__(self, number_of_generations, population_size, chromosome_length, mutation_rate, chromosome_csv_path=None):
        self.number_of_iterations = number_of_generations
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.initial_chromosome = None
        self.best_chromosome = None
        self.evolution_curve = []
        self.chromosome_csv_path = chromosome_csv_path
        # TODO:
        # rename this variable
        self.paths = []

    def solve(self):

        current_population = Population.get_random_population(self.population_size, self.chromosome_length, self.mutation_rate, self.chromosome_csv_path)
        self.init_chromosome = current_population.get_fittest_individual()

        self.best_chromosome = copy.deepcopy(self.init_chromosome)

        self.evolution_curve = []

        self.evolution_curve.append(self.best_chromosome.get_fitness_value())

        self.paths.append([city.id for city in self.best_chromosome.cities])

        for _ in range(self.number_of_iterations):
            new_population = current_population.evolve_population()
            new_chromosome = new_population.get_fittest_individual()
            
            if new_chromosome < self.best_chromosome:
                self.best_chromosome = copy.deepcopy(new_chromosome)

            self.evolution_curve.append(self.best_chromosome.get_fitness_value())

            self.paths.append([city.id for city in self.best_chromosome.cities])

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
    
    def plotTSP(self, paths, points, num_iters=1):

        # paths: list of paths, each path is a permutation of numbers
        # points: array of tuples, (x, y)
        # num_iters: number of paths
        
        """
        path: List of lists with the different orders in which the nodes are visited
        points: coordinates for the different nodes
        num_iters: number of paths that are in the path list
        
        """

        # Unpack the primary TSP path and transform it into a list of ordered 
        # coordinates

        x = []; y = []
        for i in paths[0]:
            x.append(points[i][0])
            y.append(points[i][1])
        
        plt.plot(x, y, 'co')

        # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
        a_scale = float(max(x))/float(100)

        # Draw the older paths, if provided
        if num_iters > 1:

            for i in range(1, num_iters):

                # Transform the old paths into a list of coordinates
                xi = []; yi = [];
                for j in paths[i]:
                    xi.append(points[j][0])
                    yi.append(points[j][1])

                plt.arrow(xi[-1], yi[-1], (xi[0] - xi[-1]), (yi[0] - yi[-1]), 
                        head_width = a_scale, color = 'r', 
                        length_includes_head = True, ls = 'dashed',
                        width = 0.001/float(num_iters))
                for i in range(0, len(x) - 1):
                    plt.arrow(xi[i], yi[i], (xi[i+1] - xi[i]), (yi[i+1] - yi[i]),
                            head_width = a_scale, color = 'r', length_includes_head = True,
                            ls = 'dashed', width = 0.001/float(num_iters))

        # Draw the primary path for the TSP problem
        plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale, 
                color ='g', length_includes_head=True)
        for i in range(0,len(x)-1):
            plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
                    color = 'g', length_includes_head = True)

        #Set axis too slitghtly larger than the set of x and y
        plt.xlim(0, max(x)*1.1)
        plt.ylim(0, max(y)*1.1)
        plt.show()