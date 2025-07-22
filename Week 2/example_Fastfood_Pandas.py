import pandas as pd

#  Read csv file to DataFrame
#  Reference: https://pandas.pydata.org/docs/dev/reference/api/pandas.read_csv.html
#  Note below, date formatting - In Pandas, DateTime is a data type that represents a single point in time. It is especially useful when dealing with time-series data like stock prices, weather records, economic indicators etc.
df = pd.read_csv('D:/My-AI-Course/Week 2/FastFoodRestaurants.csv', delimiter=",")


print(df.head())    # print first few rows
print(df.columns)   # confirm columns

print("df - data types" , df.dtypes) # print d-types of all columns
print("df.info():   " , df.info() )  # print summary of dataset

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)