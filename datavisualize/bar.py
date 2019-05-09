import matplotlib.pyplot as plt
import numpy
import math

plt.bar([1,3,5,7,9],[6,8,4,10,3], label ='lucas', color='r')
plt.bar([2,4,8,6,10],[6,8,4,10,3], label ='jonas', color='c')

plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('whoa')
plt.show()


value = numpy.random.randint(0, 100, 1000000)
max_value = max(value)
min_value = min(value)
step = int((max_value-min_value)/10 + 1)
bins = list(range(min_value, max_value, step))


plt.hist(value, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')

plt.title('random value from ' + str(min_value) + ' to ' + str(max_value) + ' by step ' + str(step))
plt.legend()
plt.show()

