import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv('D:\\My-AI-Course\\Week 2\\Assignment Solution\\US Food Restaurant Dataset\\FastFoodRestaurants.csv')

# Print full DataFrame
print("Full DataFrame:")
print(df.to_string())
print()

# Data types
print("Data Types:")
print(df.dtypes)
print()

# Info
print("DataFrame Info:")
print(df.info())
print()

# First and last 3 rows
print("First 3 rows:")
print(df.head(3))
print("\nLast 3 rows:")
print(df.tail(3))
print()

# Summary statistics
print("Summary Statistics:")
print(df.describe(include='all'))  # include='all' to include strings
print()

# Shape of DataFrame
print("Shape (rows, columns):", df.shape)
print()

# --- Column Access ---
print("Access 'name' column:")
print(df['name'])
print()

print("Access 'name' and 'city' columns:")
print(df[['name', 'city']])
print()

# --- Row Selection with loc ---
print("Single row (index 1) using .loc:")
print(df.loc[1])
print()

print("Multiple rows (index 0 and 2) using .loc:")
print(df.loc[[0, 2]])
print()

print("Slice rows 1 to 4 using .loc:")
print(df.loc[1:4])
print()

print("Conditional rows where city == 'Massena':")
print(df.loc[df['city'] == 'Massena'])
print()

# Column selection using loc
print("Column 'name' using .loc:")
print(df.loc[:2, 'name'])
print()

print("Multiple columns using .loc:")
print(df.loc[:2, ['name', 'province']])
print()

print("Column slice (city to name) using .loc:")
print(df.loc[:2, 'city':'name'])
print()

print("Conditional + column slice (province == 'NY'):")
print(df.loc[df['province'] == 'NY', 'name':'postalCode'])
print()

# --- Using index_col ---
df_indexed = pd.read_csv('D:\\My-AI-Course\\Week 2\\Assignment Solution\\US Food Restaurant Dataset\\FastFoodRestaurants.csv', index_col='keys')

print("DataFrame with 'keys' as index:")
print(df_indexed.head())
print()

# Access row by key
print("Access row by key using .loc:")
key_sample = df_indexed.index[0]  # just take first key safely
print(df_indexed.loc[key_sample])
print()

# --- iloc examples ---
print("Row 0 using iloc:")
print(df.iloc[0])
print()

print("Rows 1 and 3 using iloc:")
print(df.iloc[[1, 3]])
print()

print("Rows 1 to 3 using iloc:")
print(df.iloc[1:4])
print()

print("First column (address) using iloc:")
print(df.iloc[:, 0])
print()

print("Multiple columns using iloc:")
print(df.iloc[:, [0, 2]])
print()

print("Row and column slice using iloc:")
print(df.iloc[1:3, 0:3])
print()

# --- Add New Row ---
new_row = {
    'address': '999 New Rd',
    'city': 'Newtown',
    'country': 'US',
    'keys': 'us/newtown/999newrd/123456789',
    'latitude': 40.1234,
    'longitude': -75.1234,
    'name': 'Test Cafe',
    'postalCode': 99999,
    'province': 'TX',
    'websites': 'http://testcafe.com'
}
df.loc[len(df)] = new_row
print("DataFrame after adding a row:")
print(df.tail())
print()

# --- Drop Rows and Columns ---
df.drop([1, 3], axis=0, inplace=True)
df.drop(['websites', 'latitude', 'longitude'], axis=1, inplace=True)
print("After dropping rows 1, 3 and some columns:")
print(df.head())
print()

# --- Rename Columns ---
df.rename(columns={'province': 'state'}, inplace=True)

# Rename rows
df.rename(index={0: 101}, inplace=True)
print("After renaming column and row:")
print(df.head())
print()

# --- Query ---
print("Query: city == 'Massena' or state == 'TX'")
print(df.query("city == 'Massena' or state == 'TX'"))
print()

# --- Sorting ---
print("Sort by name:")
print(df.sort_values(by='name'))
print()

print("Sort by city and postalCode:")
print(df.sort_values(by=['city', 'postalCode']))
print()

# --- GroupBy ---
print("Group by state (count of businesses):")
grouped = df.groupby('state')['name'].count()
print(grouped)
print()

# --- Cleaning ---
df_cleaned = df.dropna()
print("Data after dropping NaNs:")
print(df_cleaned)
print()

df.fillna("N/A", inplace=True)
print("Data after filling NaN with 'N/A':")
print(df)
print()

# --- Pandas Array ---
array1 = pd.array([10, 20, 30])
print("Pandas array:", array1)

int_array = pd.array([5, 6, 7], dtype='int')
print("Typed int array:", int_array)
print()
