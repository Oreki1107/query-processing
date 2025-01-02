import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['blue', 'green', 'red', 'purple', 'orange', 'pink']

# Bar Chart with Different Colors
plt.bar(languages, popularity, color=colors)
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Bar Chart of Programming Languages Popularity with Different Colors")
plt.show()
