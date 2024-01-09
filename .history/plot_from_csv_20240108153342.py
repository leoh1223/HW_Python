import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
# df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', usecols=['Signal Length [Bit]', 'Signal Default'])
# Plot the data
plt.scatter(df['x'], df['y'])
plt.title('Scatter Plot from CSV')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
