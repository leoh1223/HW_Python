import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some data for demonstration
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
z1 = np.sin(np.sqrt(x**2 + y**2))
z2 = np.exp(-(x**2 + y**2) / 10)
z3 = x**2 - y**2

# Create a figure with multiple subplots
fig = plt.figure(figsize=(12, 8))

# Subplot 1: 2D Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), label='sin(x)', color='blue')
plt.plot(x, np.cos(x), label='cos(x)', color='red')
plt.title('2D Line Plot')
plt.legend()
plt.show()

# Subplot 2: Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(x, y, c=z1, cmap='viridis', s=50)
plt.title('Scatter Plot with Color Mapping')

# Subplot 3: 3D Surface Plot
ax = fig.add_subplot(2, 2, 3, projection='3d')
surface = ax.plot_surface(x, y, z3, cmap='plasma', linewidth=0, antialiased=False)
ax.set_title('3D Surface Plot')
fig.colorbar(surface, ax=ax, shrink=0.6, aspect=10)

# Subplot 4: Contour Plot
plt.subplot(2, 2, 4)
contour = plt.contourf(x, y, z2, cmap='magma')
plt.title('Contour Plot')
fig.colorbar(contour)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()
