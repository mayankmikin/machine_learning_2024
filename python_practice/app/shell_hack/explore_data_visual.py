import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Visualize the data

# Plot 1: Yearly Demand (km)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.barplot(x='Year', y='Demand (km)', data=demand_df)
plt.title('Yearly Demand (km)')
plt.xticks(rotation=45)

# Plot 2: Distribution of Vehicle Purchase Costs
plt.subplot(1, 2, 2)
sns.histplot(vehicles_df['Cost ($)'], bins=20, kde=True)
plt.title('Distribution of Vehicle Purchase Costs')

plt.tight_layout()
plt.show()

# Additional plot: Vehicle counts by Size
plt.figure(figsize=(8, 6))
sns.countplot(x='Size', data=vehicles_df)
plt.title('Count of Vehicles by Size')
plt.xlabel('Size')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Correlation analysis (example of correlation matrix for Demand DataFrame)
demand_corr = demand_df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(demand_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Matrix for Demand DataFrame')
plt.tight_layout()
plt.show()

# Correlation analysis for Vehicles DataFrame (if needed)
vehicles_corr = vehicles_df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(vehicles_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Matrix for Vehicles DataFrame')
plt.tight_layout()
plt.show()