import pandas as pd

# 1. Load the CSV file into a DataFrame with auto-index
df = pd.read_csv('D:\\My-AI-Course\\Week 2\\macro_monthly.csv')
print("\n--- Full DataFrame ---")
print(df)

# 2. Explore DataFrame
print("\n--- .info() ---")
print(df.info())

print("\n--- .dtypes ---")
print(df.dtypes)

print("\n--- .describe() ---")
print(df.describe())

print("\n--- .shape ---")
print(df.shape)

# 3. .to_string() with parameters
print("\n--- .to_string() with parameters ---")
print(df.to_string(
    columns=df.columns[:5],
    col_space=10,
    header=True,
    index=True,
    na_rep='Missing',
    justify='center',
    max_rows=10,
    max_cols=5,
    show_dimensions=True,
    decimal='.',
    line_width=100
))

# 4. Top 4 rows
print("\n--- Top 4 Rows ---")
print(df.head(4))

# 5. Bottom 4 rows
print("\n--- Bottom 4 Rows ---")
print(df.tail(4))

# 6. Name column - Industrial Production
print("\n--- Industrial_Production Column ---")
print(df["Industrial_Production"])

print("\n--- Manufacturers_New_Orders: Durable Goods ---")
print(df["Manufacturers_New_Orders: Durable Goods"])

# 7. Multiple columns
print("\n--- Industrial_Production & Manufacturers_New_Orders: Durable Goods ---")
print(df[["Industrial_Production", "Manufacturers_New_Orders: Durable Goods"]])

# 8. Select single row with .loc
print("\n--- .loc row 3 ---")
print(df.loc[3])

# 9. Multiple rows using .loc
print("\n--- .loc rows 3,5,7 ---")
print(df.loc[[3, 5, 7]])

# 10. Slice of rows using .loc
print("\n--- .loc rows 5 to 15 ---")
print(df.loc[5:15])

# 11. Conditional selection using .loc
print("\n--- Conditional Rows ---")
print(df.loc[(df['Year'].isin([1993, 1994, 1997])) & (df['Unemployment_Rate'] >= 1)])

# 12. Single row & multiple columns with .loc
print("\n--- .loc index 9, multiple columns ---")
print(df.loc[9, ["Industrial_Production", "Retail_Sales", 
                 "Manufacturers_New_Orders: Durable Goods", 
                 "Personal_Consumption_Expenditures"]])

# 13. Slice of rows with condition
print("\n--- Industrial_Production <= 0.5 ---")
print(df.loc[df["Industrial_Production"] <= 0.5])

# 14. Row & column conditions
print("\n--- Combined Condition ---")
print(df.loc[(df["Industrial_Production"] <= 0.5) & (df["Consumer_Price Index"] > 0.2)])

# 15. Single row with .iloc
print("\n--- .iloc 4th row ---")
print(df.iloc[4])

# 16. Multiple rows with .iloc
print("\n--- .iloc specific rows ---")
print(df.iloc[[2, 7, 8, 36, 9]])

# 17. Slice of rows with .iloc
print("\n--- .iloc rows 10 to 23 ---")
print(df.iloc[10:24])

# 18. Single column with .iloc
print("\n--- .iloc 5th column ---")
print(df.iloc[:, 4])

# 19. Multiple columns with .iloc
print("\n--- .iloc 2nd, 3rd, 8th columns ---")
print(df.iloc[:, [1, 2, 7]])

# 20. Slice of columns
print("\n--- .iloc columns 2 to 8 ---")
print(df.iloc[:, 2:9])

# 21. Combined row-column with .iloc
print("\n--- .iloc rows 4,5,7,25 & columns 3,5,7 ---")
print(df.iloc[[4, 5, 7, 25], [2, 4, 6]])

# 22. Range rows 3, 34 & cols 3 to 6
print("\n--- .iloc rows [3,34] & cols 3 to 6 ---")
print(df.iloc[[3, 34], 2:6])

# 23. Add new row
new_row = df.iloc[0].copy()
new_row["Year"] = 2050
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("\n--- After Adding New Row ---")
print(df.tail())

# 24. Delete row with index 4
df = df.drop(index=4)
print("\n--- After Deleting Row 4 ---")
print(df.head(10))

# 25. Delete rows 5 to 9
df = df.drop(index=range(5, 10))
print("\n--- After Deleting Rows 5 to 9 ---")
print(df.head(15))

# 26. Delete column “All_Employees”
if "All_Employees" in df.columns:
    df = df.drop(columns="All_Employees")
    print("\n--- After Deleting 'All_Employees' Column ---")
    print(df.head())

# 27. Delete two columns
df = df.drop(columns=["Personal_Consumption_Expenditures", "National_Home_Price_Index"])
print("\n--- After Deleting Two Columns ---")
print(df.head())

# 28. Rename column
df = df.rename(columns={"Personal_Consumption_Expenditures": 
                        "Personal_Consumption_Expenditures_Changed"})
print("\n--- After Renaming Column ---")
print(df.columns)

# 29. Rename label 5 to 8
df.rename(index={5: 8}, inplace=True)
print("\n--- After Renaming Index 5 to 8 ---")
print(df.head(10))

# 30. query()
result = df.query("`Industrial_Production` <= 0.5 and `Consumer_Price Index` > 0.2 and Year == 1992")
print("\n--- Query Result ---")
print(result)

# 31. sort by CPI
print("\n--- Sort by Consumer_Price Index ---")
df_sorted = df.sort_values(by="Consumer_Price Index")
print(df_sorted.head())

# 32. group by Year and sum Home_Price_Index
if "National_Home_Price_Index" in df.columns:
    print("\n--- Group by Year and Sum Home Price Index ---")
    print(df.groupby("Year")["National_Home_Price_Index"].sum())

# 33. dropna
print("\n--- After dropna() ---")
print(df.dropna())

# 34. fillna
print("\n--- After fillna(0) ---")
print(df.fillna(0))
