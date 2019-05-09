import matplotlib.pyplot as plt

slices = [8,7,6,3]

actvities = ['sleep', 'eating', 'working', 'playing']

cols = ['c', 'r', 'g', 'b']

plt.pie(slices, labels=actvities, colors=cols, startangle=90, shadow=True, explode=(0.05,0.05,0.05,0.05), autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()