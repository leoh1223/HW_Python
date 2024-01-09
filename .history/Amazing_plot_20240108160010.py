import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some data for demonstration
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z1 = np.sin(np.sqrt(x**2 + y**2))
z2 = np.exp(-(x**2 + y**2) / 10)
z3 = x**2 - y**2

# Create a figure with multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Subplot 1: 2D Line Plot
axs[0, 0].plot(x, np.sin(x), label='sin(x)', color='blue')
axs[0, 0].plot(x, np.cos(x), label='cos(x)', color='red')
axs[0, 0].set_title('2D Line Plot')
axs[0, 0].legend()

# Subplot 2: Scatter Plot
axs[0, 1].scatter(x, y, c=z1, cmap='viridis', s=50)
axs[0, 1].set_title('Scatter Plot with Color Mapping')

# Subplot 3: 3D Surface Plot
ax = fig.add_subplot(2, 2, 3, projection='3d')
surface = ax.plot_surface(x, y, z3, cmap='plasma', linewidth=0, antialiased=False)
ax.set_title('3D Surface Plot')
fig.colorbar(surface, ax=ax, shrink=0.6, aspect=10)

# Subplot 4: Contour Plot
axs[1, 0].contourf(x, y, z2, cmap='magma')
axs[1, 0].set_title('Contour Plot')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()
