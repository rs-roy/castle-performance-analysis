import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

myData = pd.read_csv(r'C:\Users\ranjoy\Desktop\Thesis2024\castle-performance-analysis\src\cprofile_delta400.csv')
print(myData.head())

# Plot the responses for different events and regions
sns.catplot(
    data=myData, kind="bar",
    x="k", y="t", hue="f", palette="dark", alpha=.6, height=6
)

plt.xlabel('k')
plt.ylabel('cumulative time') 

#plt.grid(True) 

#for i in ax.containers:
#    ax.bar_label(i,)

plt.show()