import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime
# Generate some data for demonstration
x1 = np.linspace(-5, 5, 100)
y1 = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x1, y1)

z1 = np.tan(np.sqrt(x**2 + y**2))
z2 = np.exp(-(x**2 + y**2) / 10)
z3 = x**2 - y**2

# Create a figure with multiple subplots
fig = plt.figure(figsize=(12, 8))

# Subplot 1: 2D Line Plot
plt.subplot(2, 2, 1)
plt.plot(x1, np.sin(x1), label='sin(x)', color='blue')
plt.plot(x1, np.cos(x1), label='cos(x)', color='red')
plt.title('2D Line Plot')
plt.legend()
# plt.show()

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
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
# Save the plot with the current time appended to the filename
file_name = f'Subplot_example{current_time}.png'
plt.savefig(file_name, dpi=300)
# plt.show()
