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

figure_top = 1000
figure_right = 100
figure_bottom = 0
figure_left = 0

rectangle_left = 30
rectangle_right = 70
rectangle_top = 700
rectangle_bottom = 300

while True:
    x = random.randint(figure_left, figure_left + (figure_right - figure_left)/2 - 1)
    y = random.uniform(figure_bottom, figure_top)
    if x > rectangle_left and y > rectangle_bottom and y < rectangle_top:
        continue
    else:
        x1_value.append(x)
        y1_value.append(y)
    if len(x1_value) > 1999:
        break

while True:
    x = random.randint(figure_left + (figure_right - figure_left)/2, figure_right)
    y = random.uniform(figure_bottom, figure_top)
    if x < rectangle_right and y > rectangle_bottom and y < rectangle_top:
        continue
    else:
        x2_value.append(x)
        y2_value.append(y)
    if len(x2_value) > 2999:
        break

'''iamge size'''
plt.figure(figsize=(10,6))

#a_value = numpy.arange(30, 30+12*math.pi, 0.2)

rectangle_hight = rectangle_top - rectangle_bottom
rectangle_width = rectangle_right - rectangle_left
figure_center_h = figure_bottom + (figure_top-figure_bottom) / 2
a_value = numpy.arange(rectangle_left, rectangle_right, 0.2)
b_value = list(rectangle_hight * math.cos((x-rectangle_left)*2 * math.pi / rectangle_width) / 2 + figure_center_h for x in a_value)
c_value = list(rectangle_hight * math.sin((x-rectangle_left)*2 * math.pi / rectangle_width - math.pi/2) / 2 + figure_center_h for x in a_value)
#b_value = list(rectangle_hight * math.cos(x*2 * math.pi / rectangle_width - math.pi/2) / 2 + figure_center_h for x in a_value)
#c_value = list(rectangle_hight * math.sin(x*2 * math.pi / rectangle_width - math.pi) / 2 + figure_center_h for x in a_value)
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

plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')

