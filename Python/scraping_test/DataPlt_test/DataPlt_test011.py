import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 101)
y = np.random.randn(101)

plt.plot(x, y, color="g")

plt.show()