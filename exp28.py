import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Horizontal Bar Chart
plt.barh(languages, popularity, color='skyblue')
plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.title("Horizontal Bar Chart of Programming Languages Popularity")
plt.show()
