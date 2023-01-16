import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

df= pd.read_csv('/Users/jiabozhu/Desktop/pricehousemed.csv')
reg_SolarEnergy = smf.ols(formula='id~ hpmdtwentyone',data=df).fit()

print(reg_SolarEnergy.summary())

y_fitted = reg_SolarEnergy.fittedvalues

fig, ax = plt.subplots(figsize=(8,6))
ax.plot('hpmdtwentyone', 'id', 'r--.',label='OLS')
plt.scatter(reg_SolarEnergy.fittedvalues, reg_SolarEnergy.resid, s = 2, alpha = 0.2, color = 'k')
plt.xlabel('hpmdtwentyone')
plt.ylabel('id')
plt.title('hpmdtwentyone of id Efficiency')

plt.show()