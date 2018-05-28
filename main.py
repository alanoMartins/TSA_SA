import re
import os.path
from experiment import Experiment


def from_file(path):
    coordinates = []
    with open(path, 'r') as f:

        name = f.readline().split(':')[1].strip()
        description = f.readline().split(':')[1].strip()
        type = f.readline().split(':')[1].strip()
        dimensions = f.readline().split(':')[1].strip()
        format = f.readline().split(':')[1].strip()
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
    return name, type, dimensions, format, coordinates


if __name__ == '__main__':
    INPUT_DIR = 'input/'
    OUTPUT_DIR = 'output/'
    DEBUG = False
    files = next(os.walk(INPUT_DIR))[2]

    for file in files:
        print('\nRUN: {}'.format(file))
        name, type_ex, dimensions, format, coord = from_file(INPUT_DIR + file)

        if int(dimensions) > 2000:
            print("Too large 4 my PC =( ")
            continue

        print("Name: {name} \nType: {type}".format(name=name, type=type_ex))
        print("Dimensions: {dimensions} \nFormat: {format} ".format(dimensions=dimensions, format=format))

        executer = Experiment(name, type_ex, dimensions, coord)
        executer.run(OUTPUT_DIR + file.split('.')[0], DEBUG)

