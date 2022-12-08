import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

df= pd.read_csv('/Users/jiabozhu/Desktop/20221208allsitenewtableevening.csv')
reg_SolarEnergy = smf.ols(formula='SolarEnergy ~ OutHum',data=df).fit()

plt.scatter(reg_SolarEnergy.fittedvalues, reg_SolarEnergy.resid, s = 2, alpha = 0.2, color = 'k')
plt.xlabel('Outdoor Humidity')
plt.ylabel('Solar Energy')
plt.title('Outdoor Humidity vs. Solar Energy Efficiency')

plt.show()