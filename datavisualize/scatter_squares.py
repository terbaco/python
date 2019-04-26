import matplotlib.pyplot as plt
import random
import math
import numpy

#x_value = list(range(1, 1001))
#y_value = [x**2 for x in x_value]

x1_value = []
x2_value = []
y1_value = []
y2_value = []
while True:
    x = random.randint(0, 49)
    y = random.uniform(1, 1000)
    if x > 25 and y > 250 and y < 750:
        continue
    else:
        x1_value.append(x)
        y1_value.append(y)
    if len(x1_value) > 2999:
        break

while True:
    x = random.randint(50, 100)
    y = random.uniform(1, 1000)
    if x < 75 and y > 250 and y < 750:
        continue
    else:
        x2_value.append(x)
        y2_value.append(y)
    if len(x2_value) > 2999:
        break

a_value = numpy.arange(25, 25+16*math.pi, 0.2)
b_value = list(250 * math.cos(x/8) + 500 for x in a_value)
c_value = list(250 * math.sin(x/8-math.pi/2) + 500 for x in a_value)
plt.scatter(a_value, b_value, c=b_value, cmap=plt.get_cmap('coolwarm'), edgecolor=None, s=12)
plt.scatter(a_value, c_value, c=c_value, cmap=plt.get_cmap('RdBu'), edgecolor=None, s=12)
plt.scatter(x1_value, y1_value, c=y1_value, cmap=plt.cm.get_cmap('hot'), edgecolor=None, s=5)
plt.scatter(x2_value, y2_value, c=y2_value, cmap=plt.cm.get_cmap('GnBu'), edgecolor=None, s=5)

'''set the title, axis and their label'''
#plt.title("sin and cos curve", fontsize=24)
#plt.xlabel("x", fontsize=20)
#plt.ylabel("value", fontsize=20)
plt.axis=None

'''set axis scale'''
#plt.tick_params(axis='both', which='major', labelsize=20)

#plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')

