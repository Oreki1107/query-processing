#Problem 9: Spearman Rank Correlation Between Study Hours and Exam Scores

import pandas as pd
from scipy.stats import spearmanr

# Sample Data
study_hours = [2, 4, 6, 8, 10]
exam_scores = [50, 55, 65, 75, 85]

# Compute Spearman Rank Correlation
def spearman_correlation(x, y):
    return spearmanr(x, y).correlation

# Example usage
print("Spearman Rank Correlation:", spearman_correlation(study_hours, exam_scores))