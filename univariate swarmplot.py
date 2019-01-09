import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
sns.swarmplot(x='day', y='tip', data=tips)
plt.ylabel('tips($)')
plt.xlabel('Day')
plt.show()
#grouping using hue
sns.swarmplot(x='day', y='tip', data=tips, hue='sex')
plt.ylabel('tips($)')
plt.xlabel('Day')
plt.show()

