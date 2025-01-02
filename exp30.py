import numpy as np
import matplotlib.pyplot as plt
# Data
groups = np.arange(5)
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Bar Width
width = 0.35

# Plotting
plt.bar(groups, means_men, width, label='Men')
plt.bar(groups + width, means_women, width, label='Women')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(groups + width / 2, ['G1', 'G2', 'G3', 'G4', 'G5'])
plt.legend()
plt.show()
