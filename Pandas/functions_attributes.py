import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('matches.csv')
print(data)          # print data of csv file
print(type(data))    # print type of data

# Functions

print(data.head())   # print first 5 rows of data for just preview (if your data set is too large)
print(data.tail())   # print last 5 rows of data for just preview

# Attribute

print(data.shape)       # print number of rows and columns of dataset 
print(data.shape[0])    # print only number of rows of dataset 
print(data.shape[1])    # print only number of columns of dataset 

# Functions

print(data.info())      # print overall preview of dataset
print(data.describe())  # prints high level mathematical summary of only numerical value columns

# Fetching columns

print(data['winner'])                       # print any column by his name 
print(data['winner'].shape)                      
print(data[['team1','team2','winner']])     # If there are more than one columns then write their names in list
print(data[['team1','team2','winner']].shape)     

# Fetching Rows and columns by iloc function

print(data.iloc[0])            # print first row 
print(data.iloc[1:3])          # print 2nd and 3rd row because 4 is not included
print(data.iloc[1:11:2])       # print even id's from one to 10
print(data.iloc[[1,5,6]])      # If there are more than one columns then write their names in list
print(data.iloc[:,[4,5,10]])   # print all rows of column 4th, 5th and 10th

# Filtration with mask

mask = data['city']=='Hyderabad'
print(data[mask]) 

mask1 = data['city']=='Hyderabad'
mask2 = data['date']>'2010-01-01'
print(data[mask1 & mask2])

print(data['winner'].value_counts())    # Print value count of any column and it works only on categorical data

# Plot Function 

print(data['winner'].value_counts().plot(kind='bar'))    # vertical bar chart
plt.show()                   
print(data['winner'].value_counts().plot(kind='barh'))    # horizontal bar chart
plt.show()                   
print(data['toss_winner'].value_counts().plot(kind='pie'))    # pie chart of toss winner column
plt.show()                   
print(data['toss_decision'].value_counts().plot(kind='pie'))    # pie chart of toss decision column
plt.show()                   
print(data['win_by_runs'].plot(kind='hist'))    # plot histogram chart of numerical values
plt.show()                   
