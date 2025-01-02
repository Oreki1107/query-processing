#Problem 5: Find All Sundays of a Given Year

import pandas as pd

# Define the function
def sundays_of_year(year):
    return pd.date_range(start=f'{year}-01-01', end=f'{year}-12-31', freq='W-SUN')

# Example usage
print("Sundays in 2024:")
print(sundays_of_year(2024))
