from Population import *
from matplotlib.animation import FuncAnimation

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
            
            if candidate_chromosome < self.best_chromosome:
                self.best_chromosome = copy.deepcopy(candidate_chromosome)

            self.evolution_curve.append(self.best_chromosome.get_fitness_value())

            self.solutions_history.append(self.best_chromosome)

            current_population = new_population
    
    def animate_solutions(self):

        x_s_coordinates, y_s_coordinates = self.init_chromosome.get_cities_coordinates()

        fig, ax = plt.subplots(nrows=1, ncols=2)

        line, = ax[0].plot([], [], lw=2)

        curve, = ax[1].plot([], [], lw=2)

        def init():

            ax[0].plot(x_s_coordinates, y_s_coordinates, 'co')

            extra_x = (max(x_s_coordinates) - min(x_s_coordinates)) * 0.05
            extra_y = (max(y_s_coordinates) - min(y_s_coordinates)) * 0.05
            ax[0].set_xlim(min(x_s_coordinates) - extra_x, max(x_s_coordinates) + extra_x)
            ax[0].set_ylim(min(y_s_coordinates) - extra_y, max(y_s_coordinates) + extra_y)

            line.set_data([], [])

        def update(frame):
            chromosome_to_plot = self.solutions_history[frame]
            ax[0].set_title('Generation: {}, fitness: {}'.format(frame, chromosome_to_plot.get_fitness_value()))
            cur_x_s = [x_s_coordinates[id] for id in chromosome_to_plot.get_cities_ids()]
            cur_y_s = [y_s_coordinates[id] for id in chromosome_to_plot.get_cities_ids()]
            line.set_data(cur_x_s, cur_y_s)

            # plot evolution
            ax[1].set_title('Evolution curve: {}'.format(frame))
            curve.set_data([frame], [self.evolution_curve[frame]])
            return line, curve

        ani = FuncAnimation(fig, update, frames=range(0, len(self.solutions_history)),
                            init_func=init, interval=3, repeat=False)
        
        plt.show()