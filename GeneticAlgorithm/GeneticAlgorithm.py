import numpy as np
import operator
import Graph
import math


class GeneticAlgorithm:

    def __init__(self, generations=100, population_size=10, tournamentSize=4, mutationRate=0.1, elitismRate=0.1):

        self.generations = generations
        self.population_size = population_size
        self.tournamentSize = tournamentSize
        self.mutationRate = mutationRate
        self.elitismRate = elitismRate
    
    def optimize(self, graph):

        population = self.__makePopulation(graph.getVertices())
        elitismOffset = math.ceil(self.population_size*self.elitismRate)

        print ("Optimizacija puta trgovca:\n{0}".format(graph))

        for generation in range(self.generations):
            print ("\nGeneracija: {0}".format(generation + 1))
            print ("Populacija: {0}".format(population))
            
            newPopulation = []            
            fitness = self.__computeFitness(graph, population)
            print ("Cene puteva:    {0}".format(fitness))
            fittest = np.argmin(fitness)

            print ("Najbolja ruta: {0} ({1})".format(population[fittest], fitness[fittest]))
            
            if elitismOffset:
                elites = np.array(fitness).argsort()[:elitismOffset]
                [newPopulation.append(population[i]) for i in elites]
                
            for gen in range(elitismOffset, self.population_size):
                parent1 = self.__tournamentSelection(graph, population)
                parent2 = self.__tournamentSelection(graph, population)
                offspring = self.__crossover(parent1, parent2)
                newPopulation.append(offspring)
                
            for gen in range(elitismOffset, self.population_size):
                newPopulation[gen] = self.__mutate(newPopulation[gen])
    
            population = newPopulation

            if self.__converged(population):
                break

        return (population[fittest], fitness[fittest])


    def __makePopulation(self, graph_nodes):
        return [''.join(v for v in np.random.permutation(graph_nodes)) for i in range(self.population_size)]
    
    def __computeFitness(self, graph, population):
        return [graph.getPathCost(path) for path in population]
    
    def __tournamentSelection(self, graph, population):

        tournament_contestants = np.random.choice(population, size=self.tournamentSize)
        tournament_contestants_fitness = self.__computeFitness(graph, tournament_contestants)
        return tournament_contestants[np.argmin(tournament_contestants_fitness)]
    

    def __crossover(self, parent1, parent2):

        offspring = ['' for allele in range(len(parent1))]
        index_low, index_high = self.__computeLowHighIndexes(parent1)
        
        offspring[index_low:index_high+1] = list(parent1)[index_low:index_high+1]
        offspring_available_index = list(range(0, index_low)) + list(range(index_high+1, len(parent1)))        
        for allele in parent2:
            if '' not in offspring:
                break
            if allele not in offspring:
                offspring[offspring_available_index.pop(0)] = allele
        return ''.join(v for v in offspring) 


    def __mutate(self, genome):

        if np.random.random() < self.mutationRate:
            index_low, index_high = self.__computeLowHighIndexes(genome)
            return self.__swap(index_low, index_high, genome)
        else:
            return genome


    def __computeLowHighIndexes(self, string):

        index_low = np.random.randint(0, len(string)-1)
        index_high = np.random.randint(index_low+1, len(string))
        while index_high - index_low > math.ceil(len(string)//2):
            
            try:
                index_low = np.random.randint(0, len(string))
                index_high = np.random.randint(index_low+1, len(string))
            except ValueError:
                pass
        return (index_low, index_high)


    def __swap(self, index_low, index_high, string):

        string = list(string)
        string[index_low], string[index_high] = string[index_high], string[index_low]
        return ''.join(string)


    def __converged(self, population):     
        return all(genome == population[0] for genome in population)

if __name__ == '__main__':
    
    graph = Graph.Graph()
    graph.setAdjacent('a', 'b', 7)
    graph.setAdjacent('a', 'c', 6)
    graph.setAdjacent('a', 'd', 10)
    graph.setAdjacent('a', 'e', 13)
    graph.setAdjacent('b', 'c', 7)
    graph.setAdjacent('b', 'd', 10)
    graph.setAdjacent('b', 'e', 10)
    graph.setAdjacent('c', 'd', 8)
    graph.setAdjacent('c', 'e', 9)
    graph.setAdjacent('d', 'e', 6)

    GA = GeneticAlgorithm(generations=20, population_size=7, tournamentSize=2, mutationRate=0.2, elitismRate=0.1)
    
    optimal_path, path_cost = GA.optimize(graph)
    
    print ("\nNajbolja ruta: ", optimal_path)
    print ("Cena: ", path_cost)
