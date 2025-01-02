import pandas as pd

# Load dataset
df = pd.read_csv('world_alcohol.csv')  # Replace with your file path

# Get dimensions and columns
print("Shape:", df.shape)
print("Columns:", df.columns)
