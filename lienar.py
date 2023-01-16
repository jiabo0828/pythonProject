import pandas as pd
from scipy import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jiabozhu/Desktop/fsds-gw/12346.csv')

X = df[['Numberofhouseholds', 'Householdsize1person']]
y = df['airbnbhouse']

regr = linear_model.LinearRegression()
model = regr.fit(X, y)

print('Intercept:', model.intercept_)
print('Coefficients:', model.coef_)

plt.show()