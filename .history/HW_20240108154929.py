import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime

# Create a meshgrid of x and y values
x = np.linspace(-5, 1, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define a function to generate z values (example: a saddle shape)
z = x**2 - y**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(x, y, z, cmap='viridis')

# Add a colorbar
fig.colorbar(surface, ax=ax, shrink=0.6, aspect=10)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title
ax.set_title('3D Surface Plot')
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# Save the plot with the current time appended to the filename
file_name = f'example_plot_{current_time}.png'
plt.savefig(file_name, dpi=300)

# Show the plot
# plt.savefig('3d_surface_plot.png', dpi=300)  # Specify the filename and optional DPI
# plt.show()

