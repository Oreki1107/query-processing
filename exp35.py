import matplotlib.pyplot as plt

# Sample Data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

# Scatter Plot
plt.scatter(math_marks, science_marks, color='red')
plt.title('Math vs Science Marks')
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.show()
