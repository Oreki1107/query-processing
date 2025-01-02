#Problem 10: Compare Customer Names Using FuzzyWuzzy

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Sample Data
dataset1 = ['John Smith', 'Jane Doe', 'Michael Johnson']
dataset2 = ['Jon Smith', 'Janne Doe', 'Mike Johnson']

# Compare and Find Matches
def compare_customer_names(names1, names2):
    results = []
    for name1 in names1:
        best_match = process.extractOne(name1, names2)
        results.append((name1, best_match[0], best_match[1]))
    return results

# Example usage
matches = compare_customer_names(dataset1, dataset2)
for match in matches:
    print(f"Original: {match[0]}, Matched: {match[1]}, Score: {match[2]}")