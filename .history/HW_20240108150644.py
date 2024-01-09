
import numpy as np
import matplotlib.pyplot as plt
#import tkinter as tk
plt.close()
# Generate 100 random numbers between 0 and 1
random_data = np.random.rand(10000)

# Plot the random data
plt.scatter(range(len(random_data)), random_data)
plt.title("Scatter Plot")
plt.xlabel("Data Point")
plt.ylabel("Random Value")
plt.show()
