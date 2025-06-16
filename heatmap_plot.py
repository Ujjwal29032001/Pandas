import numpy as np
import matplotlib.pyplot  as plt
# data = np.random.rand(10,10)
# data1 = np.array([[10,20,30,40],[40,50,60,70]])
# # plt.imshow(data, cmap='hot',interpolation='nearest')
# plt.imshow(data1, cmap='hot',interpolation='nearest')
# plt.colorbar()
# plt.show()

# data = [np.random.normal(0,std,100) for std in range(1,4)]
# plt.violinplot(data)
# plt.show()
# stacked_bar_plot
labels = ['A','B','C']
labels1 = ['a','b','c']
y1 = [5,10,15]
y2 = [3,6,9]
# plt.bar(labels,y1)
# plt.bar(labels,y2)
plt.bar(labels,y1,label='Group 1')
plt.bar(labels1,y2,label='Group 2')
# plt.bar(labels,y1,label='Group 1')
# plt.bar(labels,y2,bottom=y1,label='Group 2')
plt.legend()
plt.show()

import matplotlib.plt as py
import 