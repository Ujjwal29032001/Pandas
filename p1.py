# import pandas as pd
# ind=['a','b','c','d','e']

# ser = pd.Series([10,20,30,40,50],index=ind)
# print(ser)
# # print(ser.loc[0])
# # print(ser.loc[1])
# # print(ser.loc[2])
# # print(ser.loc[3])
# # we use loc method for find the value on indexing  

# # res = ser.loc[0:3] #indexing of slicing
# # print(res) 

# '''print(ser.loc['a'])   #label based indexing
# print(ser.loc['b'])   #label based indexing
# print(ser.loc['c'])   #label based indexing
# print(ser.loc['d'])   #label based indexing
# print(ser.loc['e'])   #label based indexing
# print(ser.iloc[0])     #iloc indexing  
# print(ser.iloc[1])     #iloc indexing  
# print(ser.iloc[2])     #iloc indexing  
# print(ser.iloc[3])     #iloc indexing  
# print(ser.iloc[4])     #iloc indexing  

# print(ser['a']) 

# data = ser + 100
# print(data) '''

# # data1 = ser+100
# # data2 = ser/5
# # data3 = ser-40
# # print(data1)
# # print(data2)
# # print(data3)

# ser1 = pd.Series([2,4,6,8,10])
# ser2 = pd.Series([3,6,9,2,15])
# '''res = ser1 + ser2  
# res1 = ser1 / ser2 
# res2 =  ser1 * ser2 
# res3 = ser1 - ser2 
# print(res)
# max_ele = ser1.max()
# min_ele = ser1.min()
# sum_ele = ser.sum()
# print(max_ele)
# print(min_ele)
# print(sum_ele)'''
# # avg_ele = ser1.mean()
# # print(avg_ele)

# # middle_value = ser1.median()
# # print(middle_value) 

# # res = ser1>4
# # print(res)

# # res = ser1>=4
# # print(res) 

# res = (ser1.dtype)
# res1 = (ser1.size)
# print(res)
# print(res1) 
# =======

# DATA FRAME in Pandas
import pandas as pd 
# ind = ['a','b','c','d']

# data = {
#     'Name':['Douglas','KImball','John','leon'],
#     'City':['Kansas','Macau','Vegas','Barcelona'],
#     'Age':[29,25,31,30] 
# }
# df = pd.DataFrame(data,index=ind)
# print(df)
# print(df['Name'])
# print(df['Age'])
# print(df['City']) 

# print(df[['Name','Age']])
# print(df.loc[0])

# print(df.loc[1])
# print(df.loc[2])
# print(df.loc[0])
# print(df.loc[3])


# print(df.loc['a'])
# print(df.loc['b'])
# print(df.loc['c'])
# print(df.loc['d'])

# res = (df.iloc[0:3,['Name','Age']])
# print(res)


# emp = {
#     'emp_id':['cb101','cb102','cb103','cb104','cb105'],
#     'name':['john','Maxima','Augstine','Charlie','Emmanuel'],
#     'age':[25,48,49,78],
#     'salary':[5000,4000,700,4000]
# }
# employee = pd.DataFrame(emp)
# employee.to_csv('data.csv')
# print(employee)
# max_age=employee['age'].max()
# min_age=employee['age'].min()
# avg_age=employee['age'].mean()
# mid_age=employee['age'].median()
# count_age = employee['age'].count()

# print("max age of employee",max_age)
# print("min age of employee ",min_age)
# print("avg of employee",avg_age)


# print("mid age of employee ",mid_age)
# print("how many age data avaialbale in rec",count_age)

# print("salary wise rec")  
# max_sal = employee['salary'].max()
# min_sal = employee['salary'].min()
# avg_sal = employee['salary'].mean()
# mid_sal = employee['salary'].median()
# total_sal = employee['salary'].sum()
# standard_sal = employee['salary'].std()
# var_sal = employee['salry'].var()


# print("Employee max salary ",max_sal)
# print("Employee min sal",min_sal)
# print("employee avg salary",avg_sal)
# print("employee of mid slary",mid_sal)
# print("employee total salry",total_sal)
# print("variance of salary",standard_sal)
# print("",var_sal)
# ==============================================

# employee = pd.read_csv('employee.csv')
# emp_sal = employee[['salary','Employee_ID']]
# print(emp_sal)

# count of employess = employee.groupby('JOB_ID')['Salary'].sum()
# print(count of employees)

# derp_wise_sal = employee.groupby('Department_ID')['SALARY'].sum()
# print(count_of_employee)
# print(deprt_wise_salary)

# print(df.head(0))
# rec = df[['FIRST_NAME','LAST_NAME']]
# print(rec)
# import pandas as pd
# emp = {
#     'Roll_No':['cb101','cb102','cb103','cb104','cb105'],
#     'Name':['Abgelina','Bob','Janey','Kim','Stalin'],
#     'age':[25,26,28,92,45],
#     'Salary':[12000,72000,19500,4800,7800]

# }
# employee = pd.DataFrame(emp)
# print(employee)

# max_age = employee['age'].max()
# min_age = employee['age'].min()
# avg_age = employee['age'].mean()
# mid_age = employee['age'].median()
# total_age = employee['age'].sum()
# print("Maximum Salary : ",max_age)
# print("Minimum Salary : ",min_age)
# print("Average Age : ",avg_age)
# print("Median Value : ",mid_age)
# print("Total age : ",total_age)


# max_sal = employee['Salary'].max()
# min_sal = employee['Salary'].min()
# avg_sal = employee['Salary'].mean()
# mid_sal = employee['Salary'].median()
# total_sal = employee['Salary'].sum()
# unique_sal = employee['Salary'].unique()
# print("Maximum Salary : ",max_sal)
# print("Minimum Salary : ",min_sal)
# print("Average Salary : ",avg_sal)
# print("Median Salary : ",mid_sal)
# print("Total Salary : ",total_sal)

# import pandas as pd
# data  ={
#     'name':['Shivam','Ujjwal','Shinu','Nanku','Shambu'],
#     'age':[25,29,45,78,91],
#     'city':['Barcelona','Madrid','Tokyo','Singaore','Hawaii'],
#     'salary':[20000,30000,40000,60000]
# }
# df=pd.DataFrame(data)
# for index,row in df.iterrows():
#     print(f'index:{index} Name :{row['name']} Age:{row['age']} city:{row['city']}')
#     print(row)   

# print("iter Tuples use here ")
# for row in df.itertuples():
#     print(f'index{row.Index}  name:{row.name}   age:{row.age} city:{row.city}')
#     #   key . column name 
#     print(row)


# for i,j in df.items():
#     print(f'Column name : {i}    data:{j.tolist()}')

# df = pd.read_csv('employees.csv')
# for i ,j in df.items():
#     print(f'Column name : {i} Values :{j.tolist()}')


# print(df.head(0))


# for row in df.itertuples():
#     print(f'Emp_id:{row.EMPLOYEE_ID} Salary:{row.SALARY}') 

# data  ={
#     'name':['Shivam','Ujjwal','Shinu','Nanku','Shambu'],
#     'age':[25,29,45,78,91],
#     'city':['Barcelona','Madrid','Tokyo','Singapore','Hawaii'],
#     'salary':[20000,30000,40000,60000,78000]
# }

# df = pd.DataFrame(data)
# df['tax']=df['salary'].apply(lambda x:x*0.10)
# print(df) 

# sal_inc = df['salary'].apply(lambda x:x*0.10)
# df['gs'] = df['salary']+ sal_inc

# print(df)  

# df.to_csv('emp_inc2.csv',index=False)

# map function used
# df['age_group']  = df['age'].map(lambda x: 'young' if x< 30  else 'adult')
# print(df) 

# df['sal_incre'] = df['salary'].map(lambda x:x*0.10 if x <= 40000 else x *0.20)
# print(df)

# df2 = df.applymap(lambda x:x if isinstance(x,str)  else
# ================================================  
import pandas as pd
data  ={
    'name':['Shivam','Ujjwal','Shinu','Nanku','Shambu'],
    'age':[25,29,45,78,91],
    'city':['Barcelona','Madrid','Tokyo','Singapore','Hawaii'],
    'salary':[20000,30000,40000,60000,78000]
}
x = '10'
y = 'a' 
if isinstance(x,str):
    res = x 
    print(res) 
else:
    res = 0.10*x
    print(res)    