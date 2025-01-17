import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

# Define points
points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
])

# Perform Delaunay triangulation
simplices = Delaunay(points).simplices

# Plot the triangulation
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.title("Delaunay Triangulation")
plt.xlabel("X")
plt.ylabel("Y")

# Save or show the plot
plt.savefig("triangulation_plot.png")  # Saves the plot to a file
plt.show()  # Displays the plot
