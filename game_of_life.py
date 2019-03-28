import numpy as np
import sys
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib import colors as clr
import matplotlib.patches as mpatches

state = ('Dead', 'Alive')

class GameOfLife:
    def __init__(self, N=100):
        # Initilize the grid
        self.N = N
        self.grid = np.random.randint(low=0, high=2, size=(N,N))

    def update_values(self, frames, image, grid, N):
        NewGrid = grid.copy()

        # Get the neighbors value
        for line in range(NewGrid.shape[0]):
            for column in range(NewGrid.shape[1]):
                value = grid[(line-1)%N,(column-1)%N] + grid[(line-1)%N,column] + grid[(line-1)%N,(column+1)%N] + grid[line,(column-1)%N] + grid[line,(column+1)%N] + grid[(line+1)%N,(column-1)%N] + grid[(line+1)%N,column] + grid[(line+1)%N,(column+1)%N]

                # Apply Cornswall Law's
                if grid[line,column] == 1:
                    if value > 3 or value < 2:
                        NewGrid[line,column] = 0
                else:
                    if value == 3:
                        NewGrid[line,column] = 1

        # Update the grid values
        image.set_data(grid)
        grid[:] = NewGrid[:]

        return image

    def main(self):
        # Set image figure
        fig, ax = plt.subplots()
        image = ax.imshow(self.grid, cmap=clr.ListedColormap(['black', 'green']), interpolation='nearest')

        #Set figure legend
        values = np.unique(self.grid.ravel())
        colors = [image.cmap(image.norm(value)) for value in values]
        patches = [mpatches.Patch(color=colors[i], label="{l}".format(l=state[i]) ) for i in range(len(values))]
        plt.legend(handles=patches, bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.5)
        plt.title("Execution with Grid = " + str(self.N))

        # Start de animated figure
        anim = animation.FuncAnimation(fig, self.update_values, fargs=(image, self.grid, self.N), frames=20, interval=100)
        plt.show()

if __name__ == "__main__":
    gol = GameOfLife(N=100)
    gol.main()
