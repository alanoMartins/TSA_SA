import matplotlib.pyplot as plt
import numpy as np

class Painter():

    def plot_path(self, best_solution, coords):
        self.plotTSP([best_solution], coords)

    def plot_costs(self, costs):
        x_axes = np.linspace(0, len(costs), len(costs))
        plt.plot(x_axes, costs, color='red')
        plt.ylabel('Costs')
        plt.xlabel('Execution')
        plt.show()

    def plotTSP(self, paths, points, num_iters=1):

        """
        Obtido do gist desse artigo:
        http://www.blog.pyoung.net/2013/07/26/visualizing-the-traveling-salesman-problem-using-matplotlib-in-python/

        """

        # Unpack the primary TSP path and transform it into a list of ordered
        # coordinates

        x = [];
        y = []
        for i in paths[0]:
            x.append(points[i][0])
            y.append(points[i][1])

        plt.plot(x, y)

        # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
        a_scale = float(max(x)) / float(100)

        # Draw the older paths, if provided
        if num_iters > 1:

            for i in range(1, num_iters):

                # Transform the old paths into a list of coordinates
                xi = [];
                yi = [];
                for j in paths[i]:
                    xi.append(points[j][0])
                    yi.append(points[j][1])

                plt.arrow(xi[-1], yi[-1], (xi[0] - xi[-1]), (yi[0] - yi[-1]),
                          head_width=a_scale, color='r',
                          length_includes_head=True, ls='dashed',
                          width=0.001 / float(num_iters))
                for i in range(0, len(x) - 1):
                    plt.arrow(xi[i], yi[i], (xi[i + 1] - xi[i]), (yi[i + 1] - yi[i]),
                              head_width=a_scale, color='r', length_includes_head=True,
                              ls='dashed', width=0.001 / float(num_iters))

        # Draw the primary path for the TSP problem
        plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width=a_scale,
                  color='b', length_includes_head=True)
        for i in range(0, len(x) - 1):
            plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]), head_width=a_scale,
                      color='b', length_includes_head=True)

        # Set axis too slitghtly larger than the set of x and y
        plt.xlim(min(x) * 1.1, max(x) * 1.1)
        plt.ylim(min(y) * 1.1, max(y) * 1.1)
        plt.show()
