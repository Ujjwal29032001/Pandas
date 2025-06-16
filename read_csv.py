import pandas as pd
employees = pd.read_csv('employees.csv')
# emp_sal = employees['SALARY']
# print(emp_sal)

# emp_sal = employees['SALARY'].sum()
# print(emp_sal)

# count_of_employees = employees.groupby('JOB_ID')['SALARY'].unique()
# print(count_of_employees)

# count_of_employees = employees.groupby('JOB_ID')['SALARY'].min()
# print(count_of_employees)

# dept_wise_sal = employees.groupby('DEPARTMENT_ID')['SALARY'].sum()
# print(dept_wise_sal)
# dept_wise_sal = employees.groupby('DEPARTMENT_ID')['SALARY'].mean()
# print(dept_wise_sal)
# dept_wise_sal = employees.groupby('DEPARTMENT_ID')['SALARY'].median()
# print(dept_wise_sal)
# dept_wise_sal = employees.groupby('DEPARTMENT_ID')['SALARY'].count()
# print(dept_wise_sal)

# rec = employees[['FIRST_NAME','LAST_NAME']]
# print(rec) 

# print(employees.head(0))

