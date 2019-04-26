import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36]
tub = [0, 1, 8, 27, 64, 125, 216]
fun1=[4,9,16,25,36]
plt.plot(squares, tub, linewidth=5)
plt.plot(fun1, linewidth=10)
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()