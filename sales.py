import pandas as pd

import matplotlib.pyplot as plt
data = {
    'Month': ['Jan','Feb','Marc','April','May'],
    'Product A': [150,200,450,360,178],
    'Product B': [450,890,140,220,460],
    'Product C' : [410,123,220,789,145]
}

df = pd.DataFrame(data)
print(df) 

df.plot(kind='bar',xlabel="Months",ylabel="Product",title="Sales Data")
plt.show()
