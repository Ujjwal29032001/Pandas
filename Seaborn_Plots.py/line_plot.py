import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd
# line Plot used  

# trip = pd.DataFrame({
#     'tip':['mon','tue','wed','fri'],
#     'total_bill':[1000,2000,3000,4000]
    
# })
# sns.lineplot(x="tip",y="total_bill",data=trip)
# plt.subplot(2,1,2)


# #bar_plot
# trip = pd.DataFrame({
#     'day':['mon','tue','Wed','Fri'],
#     'total_bill':[1000,2000,3000,4000]
# })
# sns.barplot(x='day',y="total_bill",data=trip)
# plt.subplot(2,1,2)
# plt.show()

# # Histogram 
trip = pd.DataFrame({
    'day':['mon','tue','wed','fri'],
    'total_bill':[1000,2000,3000,6000]
})


# sns.histplot(trip['total_bill'])
# plt.show() 

# box plot
# trip = pd.DataFrame({
#     'day':['mon','tue','wed','fri'],
#     'total_bill':[1000,2000,3000,6000]
# })
# sns.boxplot(x="day",y="total_bill",data=trip)
# plt.show() 

# heatmap plot
# data = np.array([[10,20,30],[40,50,60]])
# sns.heatmap(data)


