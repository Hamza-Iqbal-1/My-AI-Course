import pandas as pd

# Load the CSV file with required columns only
df = pd.read_csv('RealEstate-USA.csv', usecols=["brokered_by", "price", "acre_lot", "city", "house_size", "street", "zip_code", "state", "bed", "bath"])

# Show the first few rows to confirm
print(df.head())

# 1. Info about DataFrame
print("=== .info() ===")
print(df.info())

# 2. Data types of each column
print("\n=== .dtypes ===")
print(df.dtypes)

# 3. Descriptive statistics
print("\n=== .describe() ===")
print(df.describe())

# 4. Shape of DataFrame (rows, columns)
print("\n=== .shape ===")
print(df.shape)

# Print the entire DataFrame, even if it’s long (unlike default printing which shows only the first/last few rows).
print(df.to_string())

# Apply .to_string() with various parameters
output = df.to_string(
    buf=None,  # Outputs to string (not to a file)
    columns=["price", "house_size", "city"],  # Select subset of columns
    col_space=12,  # Minimum width of each column
    header=True,  # Show header row (column names)
    index=False,  # Do not print row indices
    na_rep="Missing",  # Replace NaN with this string
    formatters={
        "price": "${:,.0f}".format,  # Format price with dollar sign & comma
        "house_size": "{:.0f} sqft".format  # Add sqft suffix
    },
    float_format="{:.2f}".format,  # Format for float values (fallback)
    sparsify=False,  # Useful if you have MultiIndex (shows all levels)
    index_names=True,  # Show index name (if index has a name)
    justify="center",  # Center-align headers
    max_rows=15,  # Show only 15 rows
    max_cols=3,  # Show only 3 columns (if more, truncates)
    show_dimensions=True,  # Appends (rows x cols) info at bottom
    decimal=",",  # Use comma as decimal separator (European style)
    line_width=100  # Wrap line after 100 characters
)

print(output)

# Bottom 9 rows
bottom_9 = df.tail(9)
print(bottom_9)

# Full "city" column
print(df["city"])

# Full "street" column
print(df["street"])

# Multiple columns: "street" and "city"
print(df[["street", "city"]])

# Selecting row at index 5
row_5 = df.loc[5]
print("Row at index 5:\n", row_5)

# Selecting rows at index 3, 5, 7
rows_multiple = df.loc[[3, 5, 7]]
print("Rows at index 3, 5, 7:\n", rows_multiple)

# Selecting a range of rows from index 3 to 9 (inclusive)
rows_range = df.loc[3:9]
print("Rows from index 3 to 9:\n", rows_range)

# Selecting rows with price > 100000
price_gt_100k = df.loc[df['price'] > 100000]
print("Rows where price > 100000:\n", price_gt_100k)

# Selecting rows where city is 'Adjuntas'
city_adjuntas = df.loc[df['city'] == 'Adjuntas']
print("Rows where city is 'Adjuntas':\n", city_adjuntas)

# Selecting rows with both conditions
adjuntas_filtered = df.loc[(df['city'] == 'Adjuntas') & (df['price'] < 180500)]
print("Rows where city is 'Adjuntas' and price < 180500:\n", adjuntas_filtered)

# Selecting index 7 and specific columns
selected_row_cols = df.loc[7, ["city", "price", "street", "zip_code", "acre_lot"]]
print("Row 7 with selected columns:\n", selected_row_cols)

# Selecting all rows and slicing columns from 'city' to 'zip_code'
column_slice = df.loc[:, "city":"zip_code"]
print("Column slice from city to zip_code:\n", column_slice)

# Combined condition and column slice
combined_selection = df.loc[df["city"] == "Adjuntas", "city":"zip_code"]
print("Rows where city is 'Adjuntas' and columns from city to zip_code:\n", combined_selection)

# Selecting the 5th row using .iloc
row_5 = df.iloc[4]
print("17. 5th Row:\n", row_5)

# Selecting 7th, 9th, and 15th rows using .iloc
selected_rows = df.iloc[[6, 8, 14]]
print("\n18. 7th, 9th, and 15th Rows:\n", selected_rows)

# Selecting rows from 5th to 13th using .iloc
row_slice = df.iloc[4:13]
print("\n19. Rows from 5th to 13th:\n", row_slice)

# Selecting the 3rd column using .iloc
column_3 = df.iloc[:, 2]
print("\n20. 3rd Column:\n", column_3)

# Selecting 2nd, 4th, and 7th columns using .iloc
multiple_columns = df.iloc[:, [1, 3, 6]]
print("\n21. 2nd, 4th, and 7th Columns:\n", multiple_columns)

# Selecting columns from 2nd to 5th using .iloc
column_slice = df.iloc[:, 1:5]
print("\n22. Columns from 2nd to 5th:\n", column_slice)

# 23. Combined row and column selection using .iloc
rows_23 = df.iloc[[6, 8, 14], [1, 3]]
print("23. 7th, 9th, 15th row AND 2nd, 4th columns:\n", rows_23)

# 24. Combined range row and column selection using .iloc
rows_cols_24 = df.iloc[1:6:4, 1:4]
print("\n24. 2nd and 6th row, 2nd to 4th column:\n", rows_cols_24)

# 25. Add a New Row
new_row = {
    'price': 99999,
    'bed': 2,
    'bath': 1,
    'acre_lot': 0.25,
    'city': 'New City',
    'state': 'ZZ',
    'street': '999 New Street',
    'zip_code': 12345,
    'house_size': 800
}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("\n25. After adding new row:\n", df.tail(3))  # print last few rows to verify

# 26. Delete row with index 2
df = df.drop(index=2)
print("\n26. After deleting row with index 2:\n", df.head(5))

# 27. Delete rows from index 4 to 7
df = df.drop(index=range(4, 8))
print("\n27. After deleting rows index 4 to 7:\n", df.head(10))

# 28. Delete “house_size” column
df = df.drop(columns=['house_size'])
print("\n28. After deleting 'house_size' column:\n", df.columns)

# 29. Delete “house_size” and “state” columns
# Note: house_size already deleted above, we’ll assume we reloaded the original data again
# For now, only drop 'state' if it still exists
if 'state' in df.columns:
    df = df.drop(columns=['state'])
print("\n29. After deleting 'state' column:\n", df.columns)

# 30. Rename column “state” to “state_Changed”
# We'll simulate renaming on a reloaded column (if not dropped)
if 'state' in df.columns:
    df = df.rename(columns={'state': 'state_Changed'})
print("\n30. Renamed 'state' to 'state_Changed':\n", df.columns)

# 31. Rename label from 3 to 5 (row index 3 -> 5)
df = df.rename(index={3: 5})
print("\n31. Renamed row index 3 to 5:\n", df.head(10))

# 32. query() with price < 127400 and city != 'Adjuntas'
filtered_df_32 = df.query("price < 127400 and city != 'Adjuntas'")
print("\n32. Query result (price < 127400 and city != 'Adjuntas'):\n", filtered_df_32)

# 33. Sort DataFrame by price in ascending order
df_sorted = df.sort_values(by='price')
print("\n33. DataFrame sorted by price ascending:\n", df_sorted.head(10))

# 34. Group by city and sum price
grouped_price_sum = df.groupby('city')['price'].sum()
print("\n34. Group by 'city' and sum 'price':\n", grouped_price_sum)

# 35. Drop rows with any NaN values
df_cleaned = df.dropna()
print("\n35. After dropna() - rows with any NaNs removed:\n", df_cleaned)

# 36. Fill NaN values with 0
df_filled = df.fillna(0)
print("\n36. After filling NaN values with 0:\n", df_filled)
