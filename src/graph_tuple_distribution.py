import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

filename = input()
myData = pd.read_csv(filename)
print(myData.head())

# Plot the responses for different events and regions
ax = sns.barplot(x="cluster_label", y="tuple_count", data=myData)

plt.xlabel('Cluster number')
plt.ylabel('Tuple count') 

#plt.grid(True) 

#for i in ax.containers:
#    ax.bar_label(i,)


plt.show()