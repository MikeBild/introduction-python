""" Basic usage of matplotlib """

from matplotlib import pyplot as plt

# Load data series
x = [1, 3, 7]

# Plot
plt.plot(x)

# Save as PDF
plt.savefig('fig_test.pdf', dpi=600, format='pdf')

# Figure
plt.show()