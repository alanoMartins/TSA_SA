from simulated_annealing import SimulatedAnnealing
from paint import Painter

class Experiment:

    def __init__(self, name, type, dimensions, coordinates):
        self.name = name
        self.type = type
        self.dimensions = dimensions
        self.coordinates = coordinates

    def run(self, path):
        painter = Painter(path)
        simulated_annealing = SimulatedAnnealing(self.coordinates, max_interations=5000000, alpha=0.9995,
                                                 min_temperature=0.00000001)
        solution, costs = simulated_annealing.execute()

        painter.plot_path(solution, self.coordinates)
        painter.plot_costs(costs)

        print("Best solution: {}".format(solution))
        print("Costs: {}".format(costs))


