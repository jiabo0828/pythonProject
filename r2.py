

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jiabozhu/Desktop/20221208allsitenewtableevening.csv')

reg_SolarEnergy = smf.ols(formula='SolarEnergy ~ Month+TempOut',data=df).fit()

print(reg_SolarEnergy.summary())

print(reg_SolarEnergy.cov_params()) #输出系数的协方差矩阵

print(reg_SolarEnergy.conf_int()) #系数的置信区间 conf_int([alpha, cols]) 可以自己输入置信度

print(reg_SolarEnergy.HC0_se)#怀特（1980）异方差稳健标准误差

print(reg_SolarEnergy.HC1_se)# MacKinnon和White（1985）异方差稳健标准误差;从HC0_se - HC3_se

print(reg_SolarEnergy.cov_HC0)#异方差稳健协方差矩阵,从cov_HC0-cov_HC3
