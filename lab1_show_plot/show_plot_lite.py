import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 10.0, 0.0001)
y = 1 * x ** 3 + 2 * x ** 2 + 2 * x - 9 - 45 * np.sin(5 * x)

print("closest values to root:", x[(-0.1 < y) & (y < 0.1)])

fig, ax = plt.subplots()

ax.set(xlabel='x', ylabel='y',
       title='my function')
ax.plot(x, y)

ax.xaxis.grid()
ax.yaxis.grid()
# fig.savefig("test.png")
plt.show()

