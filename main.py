from simulated_annealing import SimulatedAnnealing
from paint import Painter


def load_file():
    coordinates = []

    for i in range(0, int(45)):
        line = [float(x.replace('\n','')) for x in input().split(' ')]
        print(line)
        coordinates.append([])
        for j in range(1,3):
            coordinates[i].append(line[j])

    return coordinates

if __name__ == '__main__':
    coordinates = load_file()
    simulated_annealing = SimulatedAnnealing(coordinates, max_interations=5000)
    solution, costs = simulated_annealing.execute()

    painter = Painter()

    painter.plot_path(solution, coordinates)
    painter.plot_costs(costs)

    print("Best solution: {}".format(solution))
    print("Costs: {}".format(costs))
