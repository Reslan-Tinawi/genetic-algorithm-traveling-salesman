from GeneticAlgorithm import *

def main():

    ga = GeneticAlgorithm(number_of_generations=10, population_size=200, chromosome_length=20,
                            mutation_rate=0.2, chromosome_csv_path='data/data 20 (circle).csv')
    ga.solve()
    ga.animate_solutions()

if __name__ == "__main__":
    main()