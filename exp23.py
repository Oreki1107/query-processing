import matplotlib.pyplot as plt

# Reading data from text file
x, y = [], []
with open('test.txt', 'r') as file:
    for line in file:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

# Plotting the line
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot from File")
plt.show()
