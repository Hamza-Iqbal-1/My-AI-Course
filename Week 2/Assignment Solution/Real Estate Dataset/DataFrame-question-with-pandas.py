import numpy as np
import pandas as pd

# Question 1: Create a DataFrame from Dictionary
sample_data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df1 = pd.DataFrame(sample_data)
print("Q1 - DataFrame from dictionary:\n", df1)

# Question 2: DataFrame with Specified Index Labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']
df2 = pd.DataFrame(exam_data, index=labels)
print("\nQ2 - DataFrame with index labels:\n", df2)

# Q2.1: DataFrame Info
df2.info()

# Q2.2: First 3 Rows
print("\nQ2.2 - First 3 Rows:\n", df2.iloc[:3])

# Q2.3: Select 'name' and 'score'
print("\nQ2.3 - name and score columns:\n", df2[['name', 'score']])

# Q2.4: Select specific rows and columns
print("\nQ2.4 - name and score from rows 1, 3, 5, 6:\n", df2.loc[['b', 'd', 'f', 'g'], ['name', 'score']])

# Q2.5: Attempts > 2
print("\nQ2.5 - Rows with attempts > 2:\n", df2[df2['attempts'] > 2])

# Q2.6: Count rows and columns
print("\nQ2.6 - Shape of DataFrame:\nRows:", df2.shape[0], ", Columns:", df2.shape[1])

# Q2.7: Score between 15 and 20
print("\nQ2.7 - Score between 15 and 20:\n", df2[df2['score'].between(15, 20)])

# Q2.8: Attempts < 2 and Score > 15
print("\nQ2.8 - Attempts < 2 and Score > 15:\n", df2[(df2['attempts'] < 2) & (df2['score'] > 15)])

# Q2.9: Change score in row 'd' to 11.5
df2.loc['d', 'score'] = 11.5
print("\nQ2.9 - Updated score in row 'd':\n", df2.loc['d'])

# Q2.10: Mean of scores
print("\nQ2.10 - Mean score:\n", df2['score'].mean())

# Q2.11: Append and then delete row 'k'
k_row = pd.DataFrame({
    'name': ['Sohail'], 'score': [15.0], 'attempts': [2], 'qualify': ['yes']
}, index=['k'])
df2 = pd.concat([df2, k_row])
print("\nQ2.11 - After appending row 'k':\n", df2)
df2 = df2.drop('k')
print("\nQ2.11 - After deleting row 'k':\n", df2)

# Q2.12: Sort by name descending, score ascending
sorted_df = df2.sort_values(by=['name', 'score'], ascending=[False, True])
print("\nQ2.12 - Sorted DataFrame:\n", sorted_df)

# Q2.13: Replace 'yes'/'no' with True/False
df2['qualify'] = df2['qualify'].map({'yes': True, 'no': False})
print("\nQ2.13 - Replaced qualify column:\n", df2)

# Q2.14: Change 'James' to 'Suresh'
df2['name'] = df2['name'].replace('James', 'Suresh')
print("\nQ2.14 - Replaced name 'James' with 'Suresh':\n", df2)

# Q2.15: Delete 'attempts' column
df2 = df2.drop(columns=['attempts'])
print("\nQ2.15 - Deleted 'attempts' column:\n", df2)

# Q2.16: Save to CSV with tab separator
df2.to_csv("output_tab_separated.csv", sep='\t')
print("\nQ2.16 - DataFrame written to 'output_tab_separated.csv' with tab separator")
