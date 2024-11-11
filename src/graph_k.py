import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

filename = input()
myData = pd.read_csv(filename)
print(myData.head())

# Plot the responses for different events and regions
ax = sns.barplot(x="k", y="t", palette = "Oranges_d", data=myData, errwidth=0)

plt.xlabel('k') 

plt.ylabel('execution time, t (in seconds)') 

#sns.set_style("darkgrid")

for i in ax.containers:
    ax.bar_label(i,)
plt.show()