import matplotlib.pyplot as plt

# Creating subplots
fig, axes = plt.subplots(2, 1)

axes[0].plot([1, 2, 3], [4, 5, 6])
axes[0].set_title("Plot 1")

axes[1].plot([1, 2, 3], [6, 5, 4])
axes[1].set_title("Plot 2")

plt.tight_layout()
plt.show()
