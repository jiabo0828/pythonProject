import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('/Users/jiabozhu/Desktop/lsoaairbnb20230115new.csv')

import numpy as np
X = df['Unemploymenthistory']
Y = df['id']
result1 = np.corrcoef(X, Y)

import seaborn as sns
sns.pairplot(df , hue ='Residence type: Total; measures: Value');

plt.show(markersize=0.5)











