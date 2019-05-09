import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(10000)
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()