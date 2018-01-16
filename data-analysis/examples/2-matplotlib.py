""" NumPy - usage of NumPy and MatPlotLib"""

import numpy as np
from matplotlib import pyplot as plt

# Calculate data series
x = np.arange(1, 11)
y = 2 * x + 5

# Plot
plt.title('MatPlotLib Example')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.plot(x, y, 'ob')

# Save as PNG
plt.savefig('fig_test.png', format='png')

# Figure
plt.show()