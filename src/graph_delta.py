import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

filename = input()
myData = pd.read_csv(filename)

print(myData.head())

# Plot the responses for different events and regions
sns.lineplot(x="delta", y="execution_time", markers=True, markersize=10, hue='k', style='k', palette=['magenta', 'red', 'orange'], data=myData)

plt.xlabel('delta') 

plt.ylabel('execution time, t (in seconds)') 

#sns.set_style("darkgrid")

plt.show()