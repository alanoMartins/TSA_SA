from simulated_annealing import SimulatedAnnealing
from paint import Painter
import re
import os.path
from experiment import Experiment



# def load_command():
#     coordinates = []
#
#     for i in range(0, int(45)):
#         line = [float(x.replace('\n','')) for x in re.sub("\s\s+", " ", input().strip()).split(' ')]
#         print(line)
#         coordinates.append([])
#         for j in range(1,3):
#             coordinates[i].append(line[j])
#
#     return coordinates

def from_file(path):
    coordinates = []
    with open(path, 'r') as f:

        name = f.readline().split(':')[1].strip()
        description = f.readline().split(':')[1].strip()
        type = f.readline().split(':')[1].strip()
        dimensions = f.readline().split(':')[1].strip()
        edge_weight = f.readline().split(':')[1].strip()
        initial_desct = f.readline()

        i = 0
        lines = f.readlines()
        lines = lines[:-1]
        for line in lines:
            line_clear = re.sub("\s\s+", " ", line.strip())
            line = [float(x.replace('\n', '')) for x in line_clear.split(' ')]
            coordinates.append([])
            for j in range(1, 3):
                coordinates[i].append(line[j])
            i += 1
    return name, type, dimensions, coordinates

if __name__ == '__main__':
    INPUT_DIR = 'input/'
    OUTPUT_DIR = 'output/'
    files = next(os.walk(INPUT_DIR))[2]

    for file in files:
        print('RUN: {} \n'.format(file))
        name, type_ex, dimensions, coordinates = from_file(INPUT_DIR + file)
        executer = Experiment(name, type_ex, dimensions, coordinates)
        executer.run(OUTPUT_DIR + file.split('.')[0])

    #
    # coordinates = from_file("input/ali535.tsp")
    # #coordinates = from_file("input/dataset.txt")
    # painter = Painter()
    # # painter.plot_coords(coordinates)
    # simulated_annealing = SimulatedAnnealing(coordinates, max_interations=5000000, alpha=0.9995, min_temperature=0.00000001)
    # solution, costs = simulated_annealing.execute()
    #
    #
    # painter.plot_path(solution, coordinates)
    # painter.plot_costs(costs)
    #
    # print("Best solution: {}".format(solution))
    # print("Costs: {}".format(costs))
