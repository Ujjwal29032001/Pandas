# import pandas as pd
# # Create a pandas Series with integers from 1 to 5.
# # ser = pd.Series([1,2,3,4,5])
# # print(ser)
# # print(ser.loc[0])
# # print(ser.loc[1])
# # print(ser.loc[2])
# # print(ser.loc[3])
# # print(ser.loc[4])

# # Create a pandas DataFrame from a dictionary of lists.
# # data = {
# #     "Programming":['Javascript','SeaBorn','JAVA','Swift'],
# #     "Founder":['Brendan Eich','Michael Waskom','James Gosling','Chris Lattner'],
# #     "Year":['1995','2014','1995','2010']
# # }
# # df = pd.DataFrame(data)
# # print(df['Programming'])
# # print(df['Founder'])
# # print(df['Year']) 

# # 3) Find the shape, size, and dimensions of a given pandas DataFrame.
# '''data = {
#     "Programming":['Javascript','SeaBorn','JAVA','Swift'],
#     "Founder":['Brendan Eich','Michael Waskom','James Gosling','Chris Lattner'],
#     "Year":['1995','2014','1995','2010']
# }
# df = pd.DataFrame(data)
# print(df.shape)
# print(df.size)
# print(df.ndim)''' 

# # 4)Access a specific column in a pandas DataFrame.
# # data = {
# #     "Programming":['Javascript','SeaBorn','JAVA','Swift'],
# #     "Founder":['Brendan Eich','Michael Waskom','James Gosling','Chris Lattner'],
# #     "Year":['1995','2014','1995','2010']
# # }
# # df = pd.DataFrame(data)
# # print(df["Programming"])

# # 5)Calculate the mean, median, and standard deviation of a specific column in a pandas DataFrame.
# data = {
#     "Programming":['Javascript','SeaBorn','JAVA','Swift'],
#     "Founder":['Brendan Eich','Michael Waskom','James Gosling','Chris Lattner'],
#     "Year":['1995','2014','1995','2010']
# }

# df = pd.DataFrame(data)
# df['Year']  = df['Year'].astype(int)

# mean_year = df["Year"].mean()
# median_year = df["Year"].median()
# standard_deviation = df["Year"].std()  

# print("mean",mean_year)
# print("median",median_year)
# print("Standard Deviation",standard_deviation) 

# import pandas as pd

# s = pd.Series([1,2,3,4])

# def square(x):
#     return x * x
# squared_series = s.apply(square)
# print(squared_series) 
# =================================
# 7) Reindex a pandas DataFrame to a specified index.


# df = pd.DataFrame({
#     'A':['a','b','c'],
#     'B':[1,2,3],

# }, index =[0,1,2])

# #Reindex to a new Index
# new_index = [0,1,2,3,4]
# reindex_df = df.reindex(new_index)
# print(reindex_df)

# ======================================
# 8)# Iterate over rows of a pandas DataFrame and perform a calculation on a specific column.
# df = pd.DataFrame({
#     'Name ' : ['Alice','Bob','Charlie'],
#     'Score' : [80,90,70],
# })

# # Iterate and perform Calculation add 10 bonus point to score
# for index, row in df.iterrows():
#     df.at[index,'Score'] = row['Score'] + 10
# print(df)
# #
# 9)Sort a pandas DataFrame by a specific column in ascending order.


# Sample Data Frame
# data =  {
#     'Name':['Alice','Bob','Charlie','David'],
#     'Age':[25,31,28,44]
# }
# df = pd.DataFrame(data)
# sorted_df = df.sort_values(by='Age',ascending=True)
# print(sorted_df)

# 10)Select rows from a pandas DataFrame based on a specific condition.
#Ans-10 
# data =  {
#     'Name':['Alice','Bob','Charlie','David'],
#     'Age':[25,31,28,44]
# }

# df = pd.DataFrame(data)
# print(df)

# Condition 1
# Select rows Where Age > 25
# condition1 = df[df['Age']> 25]
# print("1. Age > 25:\n",condition1)

# #Select rows Where Name starts with D
# condition2 = df[df['Name'].str.startswith('D')]
# print("\n2. Name starts with 'D':\n",condition2)

# Select row Where age is in between 25 & 30
# condition3 = df[(df['Age']>= 25) & (df['Age'] <= 30)]
# print(condition3) 

# condition4 = df[df['Name'].isin(['Alice','Eva'])]
# print(condition4) 

# Select rows Where Name does not contain 
# condition5 = df[~df['Name'].str.contains('a',case=False)]
# print(condition5)
# ================================================================

# 1)Perform a count of unique values in a pandas DataFrame column.
# import pandas as pd
# data = {
#     'City':['Delhi','Mumbai','Delhi','Chennai','Mumbai','Delhi','Kolkata']

# }
# df = pd.DataFrame(data)
# city_counts = df['City'].value_counts()
# print(city_counts) 

# 2) Group a pandas DataFrame by a specific column and calculate the sum of another column.
'''data = {
    'Department': ['Sales','HR','Sales','IT','HR','IT'],
    'Salary':[50000,40000,55000,60000,42000,62000]
}
df = pd.DataFrame(data)
grouped_sum = df.groupby('Department')['Salary'].sum()
print(grouped_sum)'''

# 3) Merge two pandas DataFrames based on a common column.
'''df1 = pd.DataFrame({
    'EmployeeId' : [1,2,3],
    'Name':['Alice','Bob','Charlie']
})

df2 = pd.DataFrame({
    'EmployeeId' : [1,2,4],
    'Salary':[50000,60000,55000]
})
merged_df = pd.merge(df1,df2, on="EmployeeId",how="inner")
print(merged_df)'''
import pandas as pd
# 4)Perform an inner join between two pandas DataFrames.
'''df_customers = pd.DataFrame({
    'CustomerId' : [1,2,3],
    'Name': ['Christian','georgia','Victor']

})
df_orders = pd.DataFrame({
    'CustomerId' : [1,2,4],
    'OrderId'  : [101,102,103]
})
result = pd.merge(df_customers,df_orders,on='CustomerId',how="inner")
print(result)'''

# 5) Convert a column in pandas DataFrame into a categorical datatype
'''df = pd.DataFrame({
    'Products' : ['Apple','Banana','Apple','Banana','Orange']
})
df['Products'] = df['Products'].astype('category')
print(df)'''

# 6)Replace missing values in a pandas DaatFrame with a specified values
'''data = {
    'Name' : ['Kelvin','Dylan','Samuel','Washington',None],
    'Age':[25,78,None,45,10],
    'City':['New York','Chicago','Singapore',None,'Los Angeles']

}
df = pd.DataFrame(data)
print("Original DataFrame : ")
print(df) 

df_filled = df.fillna(value={
    'Name':'Age Unknown',
    'Age': 0,
    'City ': 'Not Specified',
})

print("\nData Frame after replacing missing values")
print(df_filled)'''

# 7) Drop rows with misiing values from a pandas DataFrame
'''data = {
    'Name' : ['Kelvin','Dylan','Samuel','Washington',None],
    'Age':[25,78,None,45,10],
    'City':['New York','Chicago','Singapore',None,'Los Angeles']

}
df = pd.DataFrame(data)
# print("Original DataFrame : ")
# print(df) 

df_dropped = df.dropna()
print(df_dropped)'''

# 8) Calculates the sum of missing values in each column of a panads DataFrame

'''data = {
    'Name': ['Alice','Bob',None,'David'],
    'Age': [25,None,32,None],
    'City':['New York',None,None,'Chicago']
}
df = pd.DataFrame(data)
missing_values_count = df.isnull().sum()
print(missing_values_count)'''

# 9) Group a pandas DataFrame by a specific column and fill missing values with the mean of the group.
'''data = {
    'Name': ['Charlie','Bob','Evan','David','Eve'],
    'Age': [25,None,28,None,30],
    'City' : ['New York','Chicago','New York','Chicago','New York']
}
df = pd.DataFrame(data)
df['Age'] = df.groupby('City')['Age'].transform(lambda x: x.fillna(x.mean()))
print(df)'''

# 10) Perform a left join between two pandas DataFrames.
'''df1 = pd.DataFrame({
   'CustomerId' : [1,2,3,4],
   'Name': ['Allo','Pooja','Roh','Dimp']
})
df2 = pd.DataFrame({
    'CustomerId':[1,2,4],
    'Order': ['Laptop','Tablet','Phone']
})'''


