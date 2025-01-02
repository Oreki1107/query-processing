#Problem 8: Pearson’s Correlation Coefficient (rxy)

import numpy as np

# Sample Data
x = np.array([6, 8, 10])
y = np.array([12, 10, 20])

# Pearson Correlation Formula
def pearson_correlation(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
    return numerator / denominator

# Example usage
print("Pearson Correlation Coefficient:", pearson_correlation(x, y))