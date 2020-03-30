from GeneticAlgorithm import *


def main():
    ga = GeneticAlgorithm(number_of_generations=500, population_size=250, chromosome_length=20,
                          mutation_rate=0.005, chromosome_csv_path='data/data 20 (circle).csv')
    ga.solve()
    print(ga.best_chromosome)


if __name__ == "__main__":
    main()
