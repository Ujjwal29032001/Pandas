import matplotlib.pyplot as plt

# x =['A','B','C','D','E']
# y = [10,20,30,40,50]
# plt.plot(x,y,c ='r',linestyle='-',marker='^')
# plt.title('line plot')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.grid(axis='x',c='m',ls=':')
# plt.show()

# x =['A','B','C','D','E']
# y = [10,20,30,40,50]
# plt.plot(x,y,c ='r',linestyle='-',marker='o')
# plt.title('line plot')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.grid(axis='x',c='m',ls=':',lw=2)
# plt.show() 

'''x =['A','B','C','D','E']
y = [10,20,30,40,50]
z=[15,20,30,40,60]
plt.plot(x,y,'d:r')
plt.plot(x,y,'s:o')
plt.plot(x,y,'d:g',marker='d')
plt.title('line plot')
plt.xlabel('x label')
plt.ylabel('y label')
plt.grid(axis='x',c='m',ls=':',lw=2)
plt.grid(axis='y',c='b',ls=':',lw='2')
plt.legend('y')
plt.legend('z')
plt.show() '''

'''x =['A','B','C','D','E']
y = [10,20,30,40,50]
z=[15,20,30,40,60]
plt.plot(x,z,marker='s',ms=10,mfc='k',mec='r',label='data1')
plt.plot(x,z,marker='s',ms=10,mfc='k',mec='r',label='data2')
# plt.plot(x,y,'d:g',marker='d')
plt.title('line plot')
plt.xlabel('x label')
plt.ylabel('y label')
# plt.grid(axis='x',c='m',ls=':',lw=2)
# plt.grid(axis='y',c='b',ls=':',lw='2')
# plt.legend('y')
# plt.legend('z')
plt.legend()
plt.grid(axis='x',c='g',ls=':',lw=2)
plt.show() '''

'''x =['A','B','C','D','E']
y = [10,20,30,40,50]
plt.subplot(2,1,1)
plt.title('data 1 plot')
plt.xlabel('x label data')
plt.ylabel('y label data')
plt.plot(x,y,marker='s',ms=10,mfc='k',mec='r',label='data2')


a = ['F','G','H','I','J']
z=[15,16,17,20,56]
plt.subplot(2,1,2)
plt.xlabel('a label data')
plt.ylabel('z label data')
d={'family':'arial','size':20,'color':'red'}
plt.title('data 2 plot ',fontdict=d,loc='left')

plt.plot(a,z,marker='s',ms=10,mfc='k',mec='r',label='data1')
plt.legend()
plt.show()'''

'''data = [1,2,3,4,5]
plt.hist(data,bins=5)
plt.subplot(1,2,1)
d={'family':'arial','size':20,'color':'red'}
plt.title('data sales',fontdict=d)
plt.xlabel('product name B')


data1 = [5,6,7,8,9]
plt.hist(data1,bins=5)
plt.subplot(1,2,2)
d={'family':'arial','size':20,'color':'red'}
plt.title('data sales',fontdict=d)
plt.xlabel('product name B')
plt.show()'''

