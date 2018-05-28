import matplotlib.pyplot as plt
import numpy as np
import os

class Painter():

    def __init__(self, path):
        self.path = path

        if not os.path.exists(path):
            os.makedirs(path)

    def plot_path(self, best_solution, coords):
        self.plot_coords(coords)
        self.plotTSP([best_solution], coords)
        plt.savefig(self.path + '/path.png')
        # plt.show()

    def plot_coords(self, coords):
        plt.subplot(2, 1, 1)
        x, y = zip(*coords)
        plt.xlim(min(x) * 1.3, max(x) * 1.3)
        plt.ylim(min(y) * 1.3, max(y) * 1.3)
        plt.scatter(x, y)

    def plot_costs(self, costs):
        fig, ax1 = plt.subplots()
        x_axes = np.linspace(0, len(costs), len(costs))
        ax1.plot(x_axes, costs, color='b')
        plt.ylabel('Costs')
        plt.xlabel('Execution')
        fig.savefig(self.path + '/cost.png')
        # plt.show()

    def plotTSP(self, paths, points):
        plt.subplot(2, 1, 2)

        x = []
        y = []
        for i in paths[0]:
            x.append(points[i][0])
            y.append(points[i][1])

        plt.plot(x, y, color='b')
        plt.scatter(x, y, color='r')

        plt.xlim(min(x) * 1.3, max(x) * 1.3)
        plt.ylim(min(y) * 1.3, max(y) * 1.3)

