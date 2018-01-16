""" SubPlots - multiple plots """

import numpy as np
import matplotlib.pyplot as plt

# Calculate sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Setup a subplot grid that has height 2 and width 1

# Activate and plot first subplot
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')

# Activate and plot second subplot
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Figure
plt.show()