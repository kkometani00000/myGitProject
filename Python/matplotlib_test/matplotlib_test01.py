import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from scipy.stats import norm
import numpy as np

xs = np.linspace(-10, +10, 201)
ys = []
for x in xs:
    ys.append(norm.pdf(x, 0, 1))

plt.plot(xs, ys)

path = 'Python\matplotlib_test'
plt.savefig(f'{path}\matplotlib_test01_正規分布.png')
