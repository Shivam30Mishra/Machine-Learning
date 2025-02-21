import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], columns=['Column1', 'Column2', 'Column3', 'Column4'])

# some basic operations
print(df.head()) 
print(df.tail())
print(df.info())
print(df.describe())

# indexing can be done in three ways : .loc[], .iloc[], .ix[]
# columnname
print(df['Column1']) # returns a series
print(df[['Column1', 'Column2']]) # returns a DataFrame

# rowname
print(df.loc['Row1']) # returns a series
print(df.loc[['Row1', 'Row2']]) # returns a DataFrame

# rowindex
print(df.iloc[0]) # returns a series
print(df.iloc[2:4,0:2]) # returns a DataFrame

# fetching first first and last column
print(df.iloc[[0,-1] ,[0,-1]]) # returns a DataFrame

# converting DataFrame to array
print(df.iloc[:, :].values)

# Explaination of print(df.isnull().sum()) 
print(df.isnull()) #creating dataframe of same shape and value is true in each coordinates when not a number (NaN) else it gives False in that
print(df.isnull().sum())
data = {
  'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, np.nan, None, 45000]
}
df1 = pd.DataFrame(data)
print(df1.isnull().sum())

# checking the uniqueness of value in a column or row
print(df['Column1'].value_counts)
print(df['Column1'].unique())

# similar operation to np.array
print(df>2)
print(df[df['Column2']>2])