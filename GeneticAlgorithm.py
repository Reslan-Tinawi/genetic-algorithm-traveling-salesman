from Population import *
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


class GeneticAlgorithm:
    
    def __init__(self, number_of_generations, population_size, chromosome_length, mutation_rate, chromosome_csv_path=None):
        self.number_of_iterations = number_of_generations
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.init_chromosome = None
        self.best_chromosome = None
        self.evolution_curve = []
        self.chromosome_csv_path = chromosome_csv_path
        self.solutions_history = []

    def solve(self):
        
        current_population = Population.get_random_population(self.population_size, self.chromosome_length, self.mutation_rate, self.chromosome_csv_path)
        self.init_chromosome = current_population.get_fittest_individual()

        self.best_chromosome = copy.deepcopy(self.init_chromosome)

        self.evolution_curve = []

        self.evolution_curve.append(self.best_chromosome.get_fitness_value())

        self.solutions_history.append(self.best_chromosome)

        for _ in range(self.number_of_iterations):
            new_population = current_population.evolve_population()
            candidate_chromosome = new_population.get_fittest_individual()
            
            if candidate_chromosome > self.best_chromosome:
                self.best_chromosome = copy.deepcopy(candidate_chromosome)

            self.evolution_curve.append(self.best_chromosome.get_fitness_value())

            self.solutions_history.append(self.best_chromosome)

            current_population = new_population
    
    def animate_solutions(self):

        x_s_coordinates, y_s_coordinates = self.init_chromosome.get_cities_coordinates()

        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

        line1, = ax1.plot([], [], lw=2)

        line2, = ax2.plot([], [], lw=2)

        line = [line1, line2]

        evolution_x = []
        evolution_y = []

        def init():

            ax1.plot(x_s_coordinates, y_s_coordinates, 'co')

            extra_x = (max(x_s_coordinates) - min(x_s_coordinates)) * 0.05
            extra_y = (max(y_s_coordinates) - min(y_s_coordinates)) * 0.05
            ax1.set_xlim(min(x_s_coordinates) - extra_x, max(x_s_coordinates) + extra_x)
            ax1.set_ylim(min(y_s_coordinates) - extra_y, max(y_s_coordinates) + extra_y)


            extra_x = len(self.evolution_curve) * 0.05
            extra_y = (max(self.evolution_curve) - min(self.evolution_curve)) * 0.05
            ax2.set_xlim(0 - extra_x, len(self.evolution_curve) + extra_x)
            ax2.set_ylim(min(self.evolution_curve) - extra_y, max(self.evolution_curve) + extra_y)

            line[0].set_data([], [])
            line[1].set_data([], [])
            return line

        def update(frame):
            chromosome_to_plot = self.solutions_history[frame]
            ax1.set_title('Generation: {}, fitness: {}'.format(frame, chromosome_to_plot.get_fitness_value()))
            cur_x_s = [x_s_coordinates[id] for id in chromosome_to_plot.get_cities_ids()]
            cur_y_s = [y_s_coordinates[id] for id in chromosome_to_plot.get_cities_ids()]
            line[0].set_data(cur_x_s, cur_y_s)

            # plot evolution
            evolution_x.append(frame)
            evolution_y.append(self.evolution_curve[frame])
            ax2.set_title('Evolution curve: {}'.format(frame))
            line[1].set_data(evolution_x, evolution_y)
            return line

        ani = FuncAnimation(fig, update, frames=range(0, len(self.solutions_history)),
                            init_func=init, interval=3, repeat=False)
        
        plt.show()
