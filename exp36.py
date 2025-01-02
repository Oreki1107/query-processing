import matplotlib.pyplot as plt
import numpy as np

# Sample Data
group1 = (np.random.rand(10) * 50, np.random.rand(10) * 150)
group2 = (np.random.rand(10) * 50, np.random.rand(10) * 150)
group3 = (np.random.rand(10) * 50, np.random.rand(10) * 150)

# Scatter Plot
plt.scatter(group1[0], group1[1], color='red', label='Group 1')
plt.scatter(group2[0], group2[1], color='blue', label='Group 2')
plt.scatter(group3[0], group3[1], color='green', label='Group 3')
plt.title('Scatter Plot Comparing Groups')
plt.legend()
plt.show()
