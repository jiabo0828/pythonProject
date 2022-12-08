import pandas
df = pandas.read_csv('/Users/jiabozhu/Desktop/allsitenewtable12mouths.csv')

import numpy as np
X = df['Hour']
Y = df['SolarEnergy']
result1 = np.corrcoef(X, Y)
result2 = np.corrcoef(df,rowvar=False)

import scipy.stats as ss
result3 = ss.pearsonr(X, Y)
result4 = X.corr(Y)
result5 = df.corr()

import seaborn as sns
sns.pairplot(df , hue ='Hour');

from matplotlib import pyplot as plt

plt.show()











