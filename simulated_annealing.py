import math
from random import uniform, choice, randint
import random


class SimulatedAnnealing(object):
    def __init__(self, coords, alpha=0.9995, min_temperature=0.000000001, max_interations=1000):
        self.num_nodes = len(coords)
        self.alpha = alpha
        self.min_temperature = min_temperature
        self.max_interations = max_interations

        self.distances = self.__create_matrix_distance(coords)

        self.nodes = self.__initialize_nodes()

    def __initialize_nodes(self):
        return range(self.num_nodes)

    def __initialize_temperature(self):
        return math.sqrt(self.num_nodes)

    def initial_solution(self):
        '''
        Computes the initial solution (nearest neighbour strategy)
        '''
        node = random.randrange(len(self.distances))
        result = []

        nodes_to_visit = list(range(len(self.distances)))
        nodes_to_visit.remove(node)

        while nodes_to_visit:
            nearest_node = min([(self.distances[node][j], j) for j in nodes_to_visit], key=lambda x: x[0])
            node = nearest_node[1]
            nodes_to_visit.remove(node)
            result.append(node)

        return result

    # def initial_solution(self):
    #     node = choice(self.nodes)
    #     solution = [node]
    #
    #     nodes = list(self.nodes)
    #     nodes.remove(node)
    #
    #     for i in range(len(self.nodes) - 1):
    #         close_node = float('Inf')
    #         for j in nodes:
    #             if self.distances[node][j] < close_node:
    #                 close_node = self.distances[node][j]
    #
    #         #close_node = min([self.distances[node][j] for j in nodes])
    #         node = self.distances[node].index(close_node)
    #         nodes.remove(node)
    #         solution.append(node)
    #
    #     return solution

    def __randomize(self, candidate):
        l = randint(2, self.num_nodes - 1)
        i = randint(0, self.num_nodes - l)
        candidate[i:(i + l)] = reversed(candidate[i:(i + l)])
        return candidate

    def __distance(self, coord1, coord2):
        return round(math.sqrt(math.pow(coord1[0] - coord2[0], 2) + math.pow(coord1[1] - coord2[1], 2)), 4)

    def __create_matrix_distance(self, coords):
        return [[self.__distance(coords[i], coords[j]) for i in range(len(coords))] for j in range(len(coords))]

    def __cost(self, solution):
        dist = self.distances[solution[0]][solution[len(solution) - 1]]

        for i in range(1, self.num_nodes - 1):
            dist += self.distances[solution[i - 1]][solution[i]]
        return dist

    def execute(self):
        temperature = self.__initialize_temperature()
        current_solution = self.initial_solution()
        current_cost = self.__cost(current_solution)

        best_solution = list(current_solution)
        best_cost = current_cost

        costs = [current_cost]

        for i in range(self.max_interations):
            solution = self.__randomize(list(current_solution))
            cost = self.__cost(solution)
            if cost < current_cost:
                current_cost = cost
                current_solution = solution
                if cost < best_cost:
                    best_cost = cost
                    best_solution = solution
            else:
                diff_s = cost - current_cost
                if math.exp(-diff_s / temperature) > uniform(0, 1):
                    current_cost = cost
                    current_solution = solution

            temperature *= self.alpha
            costs.append(current_cost)

            if temperature <= self.min_temperature:
                break

        return best_solution, costs




