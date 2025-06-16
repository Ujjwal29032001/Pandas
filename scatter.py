import matplotlib.pyplot as plt 
# x = [1,2,3,4,5]
# y = [10,20,30,40,50]
# plt.scatter(x,y,marker='^',label='y')
# plt.grid(axis='x')
# plt.grid(axis='y')
# plt.xlabel('product name',c='g',size=30)
# plt.ylabel('product amount',c='r',size=30,)
# plt.title('sales data report',fontdict={'family':'algerian','size':30,'color':'blue'})
# plt.xticks(rotation=45)
# plt.yticks(rotation=45)
# plt.show()

# boxplot.py

# data = [1,2,5,7,8,3,5,9]
# plt.boxplot(data)
# plt.show() 

'''x = [1,2,3,4,5]
y = [10,20,30,40,50]
z = [15,25,35,45,55]
plt.scatter(x,y,marker='^',label='productA')
plt.scatter(x,z,marker='o',label='productB')
plt.grid(axis='x')
plt.grid(axis='y')
plt.xlabel('product name',c='g',size=30,)
plt.ylabel('product amount',c='r',size=30,)
plt.title('sales data report ',fontdict={'family':'algerian','size':30,'color':'purple'})'''

x = [1,2,3,4,5]
y = [1,4,6,10,6]
plt.fill_between(x,y)
plt.show()
