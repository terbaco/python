import matplotlib.pyplot as plt
import math
import numpy

fig, axes = plt.subplots(3, 2)

x = numpy.arange(1,10, 0.01)
y_1 = list(math.sin(a) for a in x )
axes[0][0].plot(x, y_1, label='sin')
axes[0][0].set_xticks([])
axes[0][0].set_yticks([])

y_2 = list(math.cos(a) for a in x )
axes[0][1].plot(x, y_2, label='cos')
axes[0][1].set_xticks([])
axes[0][1].set_yticks([])

y_3 = list(math.tan(a) for a in x )
axes[1][0].plot(x, y_3, label='tan')
axes[1][0].set_xticks([])
axes[1][0].set_yticks([])

y_4 = list(math.tanh(a) for a in x )
axes[1][1].plot(x, y_4, label='tanh')
axes[1][1].set_xticks([])
axes[1][1].set_yticks([])

y_5 = list(math.sqrt(a) for a in x)
axes[2][0].plot(x, y_5, label='sqrt')
#axes[2][0].set_xticks([])
#axes[2][0].set_yticks([])

y_6 = list(math.log10(a) for a in x)
axes[2][1].plot(x, y_6, label='log10')

plt.legend()
plt.show()