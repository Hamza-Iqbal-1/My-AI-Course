import pandas as pd

# 1. Load the CSV file (replace with your actual path)
df = pd.read_csv('D:/My-AI-Course/Week 2/Assignment Solution/Startup Growth Investment Dataset/startup_growth_investment_data.csv')

# 2. Print the DataFrame
print(df)

# 3. DataFrame Information
print("df - data types:\n", df.dtypes)
print("\ndf.info():")
print(df.info())

# 4. Head and Tail
print('\nFirst Three Rows:')
print(df.head(3))

print('\nLast Three Rows:')
print(df.tail(3))

# 5. Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# 6. Shape of the DataFrame
print("\nShape of DataFrame:", df.shape)

# 7. Access single column
startup_names = df['Startup Name']
print("\nStartup Names Column:")
print(startup_names)

# 8. Access multiple columns
startup_and_industry = df[['Startup Name', 'Industry']]
print("\nStartup and Industry Columns:")
print(startup_and_industry)

# --- .loc selections ---

# Select single row using .loc
print("\nSingle Row with .loc:")
print(df.loc[1])

# Select multiple rows using .loc
print("\nMultiple Rows with .loc:")
print(df.loc[[1, 3]])

# Select a slice of rows using .loc
print("\nSlice of Rows with .loc:")
print(df.loc[1:5])

# Conditional selection using .loc
print("\nStartups in India:")
print(df.loc[df['Country'] == 'India'])

# Select a single column using .loc
print("\nStartup Name Column (first two rows):")
print(df.loc[:1, 'Startup Name'])

# Select multiple columns using .loc
print("\nStartup and Valuation (first two rows):")
print(df.loc[:1, ['Startup Name', 'Valuation (USD)']])

# Select a slice of columns using .loc
print("\nSlice of Columns (first two rows):")
print(df.loc[:1, 'Startup Name':'Valuation (USD)'])

# Combined row and column selection
print("\nIndian Startups - Slice of Columns:")
print(df.loc[df['Country'] == 'India', 'Startup Name':'Valuation (USD)'])

# --- .iloc selections ---

# Select single row
print("\nSingle Row with .iloc:")
print(df.iloc[0])

# Multiple rows
print("\nMultiple Rows with .iloc:")
print(df.iloc[[1, 3, 5]])

# Slice of rows
print("\nSlice of Rows with .iloc:")
print(df.iloc[2:5])

# Single column
print("\nSingle Column with .iloc:")
print(df.iloc[:, 1])  # Industry

# Multiple columns
print("\nMultiple Columns with .iloc:")
print(df.iloc[:, [1, 3]])  # Industry, Investment Amount

# Slice of columns
print("\nSlice of Columns with .iloc:")
print(df.iloc[:, 1:4])  # Industry to Investment Amount

# Combined row and column selection
print("\nCombined Selection with .iloc:")
print(df.iloc[[1, 3, 5], 1:4])

# --- DataFrame Manipulation ---

# Add a new row
df.loc[len(df.index)] = ['Startup_X', 'AI', 4, 100000000.0, 400000000.0, 10, 'Pakistan', 2024, 150.5]
print("\nAfter Adding a New Row:")
print(df.tail())

# Remove rows
df.drop(index=[1, 2], inplace=True)
print("\nAfter Removing Rows (1, 2):")
print(df)

# Remove columns
df.drop(['Startup Name'], axis=1, inplace=True)
df.drop(columns='Industry', inplace=True)
print("\nAfter Dropping Columns ('Startup Name', 'Industry'):")
print(df)

# Rename columns
df.rename(columns={
    'Country': 'Country_Name',
    'Growth Rate (%)': 'Growth_Rate_Percent'
}, inplace=True)
print("\nAfter Renaming Columns:")
print(df)

# Rename row indexes
df.rename(index={0: 1000}, inplace=True)
print("\nAfter Renaming Row Index 0 → 1000:")
print(df)

# Querying data
selected_rows = df.query('`Country_Name` == "India" or `Investment Amount (USD)` > 3000000000')
print("\nQuery Result (India or High Investment):")
print(selected_rows.to_string())
print("Query Result Count:", len(selected_rows))

# Sorting
sorted_df = df.sort_values(by='Valuation (USD)')
print("\nSorted by Valuation (USD):")
print(sorted_df.to_string(index=False))

# Sorting by multiple columns
df1 = df.sort_values(by=['Valuation (USD)', 'Number of Investors'])
print("\nSorted by Valuation and No. of Investors:")
print(df1.to_string(index=False))

# Grouping by Country and summing Investment
grouped = df.groupby('Country_Name')['Investment Amount (USD)'].sum()
print("\nGrouped by Country (Total Investment):")
print(grouped)

# Cleaning missing data
df_cleaned = df.dropna()
print("\nData After dropna():")
print(df_cleaned)

# Filling NaN with zero
df.fillna(0, inplace=True)
print("\nData After fillna(0):")
print(df)

# Create Pandas arrays
arr1 = pd.array([2, 4, 6, 8])
print("\nPandas IntegerArray:", arr1)

int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print("\nInt Array:", int_array)
