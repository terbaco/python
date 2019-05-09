import matplotlib.pyplot as plt
import numpy
import math

days = range(1,25,1)

sleep = numpy.random.randint(1, 21, 24)
eating = []
working = []
playing = []

for x in sleep:
    eating_today = numpy.random.randint(1, 22-x)
    eating.append(eating_today)
    working_today = numpy.random.randint(1, 23-x-eating_today)
    working.append(working_today)
    playing_today = 24-x-eating_today-working_today
    playing.append(playing_today)

plt.stackplot(days, sleep, eating, working, playing, colors=['m','b','g','r'])
plt.xlabel('days')
plt.ylabel('hours')
plt.title('Interesting Graph\nChcek it out')
plt.show()

bins = range(1,24,1)

fig, axes = plt.subplots(2,2)
axes[0][0].hist(sleep, bins, histtype='bar', rwidth=0.8, label='sleep')
axes[0][1].hist(eating, bins, histtype='bar', rwidth=0.8, label='eating')
axes[1][0].hist(working, bins, histtype='bar', rwidth=0.8, label='working')
axes[1][1].hist(playing, bins, histtype='bar', rwidth=0.8, label='playing')

plt.legend()
plt.show()

catelog=[1,2,3,4]
fig, axes = plt.subplots(int(len(eating)/4),4, figsize=(100,500))

index = 0
for row in range(0, int(len(eating)/4)):
    for col in range(0, 4):
        axes[row][col].bar(catelog, [sleep[index], eating[index], working[index], playing[index]], label=str(index+1), colors=['c','r', 'g', 'b'])
        index+=1
plt.show()
