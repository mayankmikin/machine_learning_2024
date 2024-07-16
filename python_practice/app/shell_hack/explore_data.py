import pandas as pd

# Specify the path to the CSV files
demand_path = 'dataset/demand.csv'
vehicles_path = 'dataset/vehicles.csv'

# Load the CSV files
demand_df = pd.read_csv(demand_path)
vehicles_df = pd.read_csv(vehicles_path)

# Display the first few rows of each DataFrame to understand the structure and content
print("Demand DataFrame:")
print(demand_df.head(), "\n")

print("Vehicles DataFrame:")
print(vehicles_df.head(), "\n")

# Display summary statistics for each DataFrame
print("Summary Statistics for Demand DataFrame:")
print(demand_df.describe(), "\n")

print("Summary Statistics for Vehicles DataFrame:")
print(vehicles_df.describe(), "\n")

# Display information about the data types and non-null values
print("Info for Demand DataFrame:")
print(demand_df.info(), "\n")

print("Info for Vehicles DataFrame:")
print(vehicles_df.info(), "\n")