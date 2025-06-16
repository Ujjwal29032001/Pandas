# import pandas as pd 
# df = pd.DataFrame({
#     'Name':['Ajay','Rohan','Maxima','Minima'],
#     'Age':[25,27,31,40]
# })
# df.to_json("out_json",orient="records",indent=4)
# df_json = pd.read_json("out_json")
# print(df_json)

# import pandas as pd 
# from sqlalchemy import create_engine
# connection_string = 'mysql+pymysql://root:@localhost:3306/demodb2'
# engine = create_engine(connection_string)
# demodb2 = pd.read_json('out_json')
# demodb2.to_excel('out.xlsx',index=False)
# demodb2.to_sql('data',con=engine,if_exists="replace")
# print(
#     demodb2)


# Sample sales data for each product across mobile
'''data = {
    'Month': ['Jan','Feb','Mar','Apr','May'],
    'Product A' : [150,200,250,300,200],
    'Product B' : [100,120,180,250,145],
    'Product C' : [90,110,140,160,180],
}
df = pd.DataFrame(data)
print(df) 

df.plot(kind="line",xlabel="MonthA",ylabel="Product A",title='Sales Dtata')
plt.show() 

df.plot(kind='box',xlabel='Months',ylabel='Product',title='Sales Data')
plt.show()
   
df.plot(kind='bar',xlabel='Months',ylabel='Product',title='Sales Data')
plt.show()
   
df.plot(kind='scatter',xlabel='Months',ylabel='Product_A',title='Sales Data')
plt.show()

df.plot(kind='bar',stacked=True,xlabel='Months',ylabel='Products_Name')   
plt.show()

df.plot(kind='area',title='Monthly Sales  - Area Plot')
plt.show()

df.set_index('Month',inplace=True)
df.loc['Feb'].plot(kind='pie',title='Sales Distribution in feb',autopct=
                    
                   '%1.1f%%')
plt.show()'''


# 9) Group a pandas DataFrame by a specific column and fill missing values with the meanof the group
import pandas as pd
import matplotlib.pyplot as plt 


'''Data = ['Product1','Product2','Product3','Product4','Product5']
Sales = [1000,1500,2000,2500,3000]
plt.figure(figsize=(6,6))
plt.subplot(1,2,1)
plt.bar(Data,Sales)
d = {'family':'algerian','size':30,'color':'yellow'}
plt.title('product sales data',fontdict=d)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.xlabel('x sales')
plt.xlabel('y sales')'''


month = ['Jan','Feb','Mar','Apr','May']
Sale = [1000,1500,2000,2500,3000]
plt.subplot(1,2,2)    #1=width,2=height,1=position (row,col,index)
plt.bar(month,Sale,color='r')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.title('month sales data',fontdict=d)
Data  = ['products1','products2','products3','products4','products5']
Sales = [1000,1500,2000,2500,3000]
plt.figure(figsize=(6,6))   
plt.subplot(1,2,1) 
plt.bar(Data,Sales)
plt.show()