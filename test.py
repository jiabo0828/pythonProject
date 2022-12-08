import pandas as pd

df = pd.read_csv('/Users/jiabozhu/Desktop/allsitenewtabledate.csv')

dfrom statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

plot_acf(data=df, lags=50)

plt.show()




000000000000000





df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)

print(df.head())

close
trade_date
2005 - 01 - 04
982.794
2005 - 01 - 05
992.564
2005 - 01 - 06
983.174
2005 - 01 - 07
983.958
2005 - 01 - 10
993.879
00000000
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

from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

plot_acf(data=data, lags=50)

# Show the AR as a plot
plt.show()











