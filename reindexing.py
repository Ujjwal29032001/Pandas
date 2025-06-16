# import pandas as pd

'''index = ['d','c','b','a']
#new_index = ['a','b','c','d']
l1 = [40,30,20,10]
ser = pd.Series(l1,index=index)
print(ser)
#new_ser = ser.reindex(new_index)

new_index = ['a','d','c','e']
new_ser = ser.reindex(new_index,fill_value=20)
print("reorder ser : ",new_ser)''' 


# ind = ['1','2','3','4','5']
# data  ={
#     'name':['Shivam','Ujjwal','Shinu','Nanku','Shambu'],
#     'age':[25,29,45,78,91],
#     'city':['Barcelona','Madrid','Tokyo','Singapore','Hawaii'],
#     'salary':[20000,30000,40000,60000,78000]
# } 

# df = pd.DataFrame(data,index=ind)
# print(data)

# new_index = ['5','3','2','1','4']
# df = df.reindex(new_index)
# print(df)

'''ind = [4,3,0,1,2]
df = pd.read_csv('data.csv')
df1 = df.reindex(index=ind)
df1.to_csv('new_data.csv',index=False)

ind = [4,3,0,1,2]
df = pd.read_csv('data.csv')
print(df.loc[0])

ind = [4,3,0,1,2]
df = pd.read_csv('data.csv')
df1 = df.set_index['emp_id']
print(df)

df1 = df.set_index('name')
print(df1)
print(df1.loc['shivam'])'''


'''data  ={
    'name':['Shivam','Ujjwal','Shinu','Nanku','Shambu'],
    'age':[25,29,45,78,91],
    'city':['Barcelona','Madrid','Tokyo','Singapore','Hawaii'],
    'salary':[20000,30000,40000,60000,78000]
} 

df = pd.DataFrame(data)
print(df)
df2 = df.reindex(columns=['age','city','salary','name'])
print(df2)
df3 = df.reset_index()
print(df3)'''
# =======================================================
'''ind = ['1','2','3','4']
data = {
     'name':['Ram','Krishna','Hari','Samay'],
     'Age':[26,29,98,71],
     'City':['London','Mumbai','Tokyo','Marutuis'],
     'Salary':[15000,78000,75600,18900],
} '''
# df = pd.DataFrame(data)
# df.to_csv('data.csv')
# print(df)

# df = pd.DataFrame(data,index=ind)
# print(df)

# new_index = ['4','1','2','3']
# df = df.reindex(new_index)
# print(df)

'''ind = [3,1,0,2]
df = pd.read_csv('data.csv')
df1 = df.reindex(index=ind)
df1.to_csv('new_data.csv',index=False)'''

'''ind = [3,1,0,2]
df = pd.read_csv('data.csv')
print(df.loc[0])'''

'''ind = [3,1,0,2]
df = pd.read_csv('data.csv')
df1 = df.set_index('Age')
print(df1) 

df2 = df.set_index('name')
print(df2)
print(df2.loc['Samay']) '''

# merge_exp.py
'''
dep={
    'dp_id':[1,2,4],
    'dp_name':["IT",'SALES','Accounts'],

}
emp = {
    'emp_id':['Cb101','Cb102','Cb103'],
    'name':['ajay','vijay','Samay'],
    'dep_id':[1,2,3]
}
departments= pd.DataFrame(dep)
employee=pd.DataFrame(emp)
print(departments)
print(employee)
print("inner join records\n")
emp_rec = pd.merge(departments,employee,how='inner',left_on='dp_id',right_on='dep_id',right_index=False,
                   left_index=False)
print(emp_rec)
print("left join records\n")
emp_rec1 = pd.merge(employee,departments,how='left',left_on='dep_id',right_on='dp_id',left_index=False,right_index=False)
print(emp_rec1)
print("right join record\n")
emp_rec2 = pd.merge(employee,departments,how='right',left_on='dep_id',right_on='dp_id',left_index=False,right_index=False)
print(emp_rec2)
print("Full outer join \n")
emp_rec3 = pd.merge(employee,departments,how='outer',left_on='dep_id',right_on='dp_id',left_index=False,
right_index=False)
print(emp_rec3)

emp_rec4 = pd.merge(employee,departments,how='cross')
print(emp_rec4)'''

'''course = {
    'course_ID':[101,102,103,104],
    'Name':['BCA','MCA','BBA','MBA'],
    'fees':[25000,60000,20000,40000],
    'durations':['3years','2years','3years','2years']
}
Student = {
    'Roll_no':['Cb101','Cb102','Cb103','Cb104','Cb105'],
    'Name':['Ajay','Vijay','Samay','John','Sumit'],
    'age':[28,26,24,29,30],
    'course_ID':[102,101,103,105,106],
}
courses = pd.DataFrame(course)
Students = pd.DataFrame(Student)
print(courses)
print(Students)

college_curr = pd.merge(courses,Students,how='inner',left_on='course_ID',right_on='course_ID',left_index=False,right_index=False)
print(college_curr)
                        

college_curr1 = pd.merge(courses,Students,how='left',left_on='course_ID',right_on='course_ID',
                         left_index=False,right_index=False)
print(college_curr1)   '''


'''df = pd.DataFrame({
    'Category':['A','A','B','B','C','C'],
    'Amount':[100,150,200,250,300,350],
    'Sales':[10,20,30,40,50,60]
             
})
data = df.groupby('Category').sum()
print(data)

count_amount_sales = df.groupby('Category').count()
print(count_amount_sales)'''

'''df1 = pd.DataFrame({
    'Course':['Python','Python','React','React','Php','Php'],
    'Students':[45,40,30,20,30,15],
    'fees':[6000,6000,5000,5000,3000,3000],

})
rec = df1.groupby('Course')['Students'].sum()
print(rec)  

course_wise_fees = df1.groupby('Course')['fees'].sum()
print(course_wise_fees)

course_wise_fees = df1.groupby('Course').sum()
print(course_wise_fees)'''

'''df = pd.read_csv('employees.csv')
column_name = df.head(0)
print(column_name) 

total_cost = df['SALARY'].sum()
print(total_cost) 

department_wise_salary = df.groupby('DEPARTMENT_ID')['SALARY'].sum()
print(department_wise_salary)

job_id_wise_salary = df.groupby('DEPARTMENT_ID')['JOB_ID'].sum()
print(job_id_wise_salary)

salary_report = df.groupby('DEPARTMENT_ID')['SALARY'].agg(['max','min','mean','sum','count'])
print(salary_report)''' 

# data_rec = pd.read_csv('Product Sales Data .csv')
# print(data_rec)
# coloumn_name = data_rec.head(0)
# print(coloumn_name)

# # yearl_pro = data_rec.groupby('Cream').sum()
# # print(yearl_pro)

# month_wise_sles = data_rec.groupby('Month')[['Shampoo','Soap']].sum()
# print(month_wise_sles)

# over_all_reports=data_rec.describe()


import pandas as pd 
'''cat = ['low' ,'high', 'Medium','Low','High','low' ,'high', 'Medium','Low','High'  ]
cat_data = pd.Categorical(cat)
print(cat_data)
print(cat_data.categories)
print(cat_data.codes)

ord_list = ['Low','Medium','High']
cat_data2 = pd.Categorical(cat,categories=ord_list,ordered=True,)
print(cat_data2)
print(cat_data2.codes)
print(cat_data2.ordered)'''

df = pd.DataFrame({
    'Category':pd.Categorical(['A','B','C','A','B','C']),
    'Amount':[100,200,300,400,500]
})
print(df)
data = df.sort_values(by='Category')
print(data)

data_a = df[df['Category'] == 'A']
print(data_a)

data_b = df[df['Category'] == 'B']
print(data_b)

data_c = df[df['Category'] == 'C']
print(data_c)

data = df['Category'].value_counts()
print(data)

data = df['Category']=df['Category'].replace("A")
print(data)
 




