import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

filename = input()
myData = pd.read_csv(filename)
print(myData.head())

# Plot the responses for different events and regions
sns.lineplot(x="k", y="il", markers=True, markersize=10, hue='delta', style='delta', palette=['green', 'red'], data=myData)

plt.xlabel('k') 

plt.ylabel('information loss') 

#sns.set_style("darkgrid")

plt.show()