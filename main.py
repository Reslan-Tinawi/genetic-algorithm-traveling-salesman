from City import *
from Chromosome import *
from Population import *
from GeneticAlgorithm import *
import matplotlib.pyplot as plt
import copy
from matplotlib.animation import FuncAnimation

def animateTSP(history, points):
    ''' animate the solution over time
        Parameters
        ----------
        hisotry : list
            history of the solutions chosen by the algorith
        points: array_like
            points with the coordinates
    '''

    fig, ax = plt.subplots()

    ''' path is a line coming through all the nodes '''
    line, = plt.plot([], [], lw=2)

    def init():
        ''' initialize node dots on graph '''
        x = [points[i][0] for i in history[0]]
        y = [points[i][1] for i in history[0]]
        plt.plot(x, y, 'co')

        ''' draw axes slighty bigger  '''
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)

        '''initialize solution to be empty '''
        line.set_data([], [])
        return line,

    def update(frame):
        ''' for every frame update the solution on the graph '''
        x = [points[i][0] for i in history[frame]]
        y = [points[i][1] for i in history[frame]]
        line.set_data(x, y)
        return line

    ''' animate precalulated solutions '''

    ani = FuncAnimation(fig, update, frames=range(len(history)), init_func=init, interval=3, repeat=False)

    plt.show()

def call_plot():
    data = pd.read_csv('data/data 20 (circle).csv')
    ids = data.ids.values
    x_s = data.x.values
    y_s = data.y.values

    history = []
    for i in range(10):
        np.random.shuffle(ids)
        history.append(np.copy(ids))
    
    points = list(zip(x_s, y_s))

    animateTSP(history, points)

def main():

    ga = GeneticAlgorithm(number_of_generations=300, population_size=50, chromosome_length=20, mutation_rate=0.02, chromosome_csv_path='data/data 20 (circle).csv')
    ga.solve()
    ga.plot()
    print(ga.best_chromosome)

    # ga.plot()
    # cities_coordinates = [(city.x, city.y) for city in ga.best_chromosome.cities]
    # ga.plotTSP(ga.paths, cities_coordinates, 11)
    # animateTSP(ga.paths, cities_coordinates)
    

if __name__ == "__main__":
    main()