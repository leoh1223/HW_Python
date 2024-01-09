import numpy as np
import matplotlib.pyplot as plt

# Generate some data for demonstration
x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with a single 2D line plot
plt.figure(figsize=(8, 6))

# Plot the sine and cosine functions
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')

# Set plot labels and title
plt.title('2D Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Display legend
plt.legend()

# Show the plot
plt.show()
