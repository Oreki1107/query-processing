import matplotlib.pyplot as plt

# Data
x = [1, 2, 3]
y1 = [2, 4, 6]
y2 = [1, 3, 5]

# Plotting
plt.plot(x, y1, label='Line 1', color='blue', linewidth=2)
plt.plot(x, y2, label='Line 2', color='green', linewidth=1)
plt.legend()
plt.show()
