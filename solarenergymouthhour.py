import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('/Users/jiabozhu/Desktop/indexallSitenew.csv')

import numpy as np
X = df['THWIndex']
Y = df['SolarEnergy']
result1 = np.corrcoef(X, Y)



import seaborn as sns
sns.pairplot(df , hue ='THWIndex');



plt.show(markersize=0.5)











