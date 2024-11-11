import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

filename = input()
myData = pd.read_csv(filename)
print(myData.head())

# Plot the responses for different events and regions
ax = sns.barplot(x="t", y="S", palette = "Greens_d", orient='h', data=myData, errwidth=0, order=myData['S'])

plt.xlabel('execution time, t (in seconds)') 
plt.ylabel('sample size, S')
#sns.set_style("darkgrid")

#plt.grid(True) 

for i in ax.containers:
    ax.bar_label(i,)
plt.show()