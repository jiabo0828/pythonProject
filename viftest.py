import pandas as pd
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv('/Users/jiabozhu/Desktop/10.csv')

y, X = dmatrices('id~ Householdcomposition+Countryofbirth+Passportsheld+PopulationDensity+Householddeprivation+Yearofarrival+Lengthofresidence+Migrantindicator+Nationalidentity+Numberofhouseholds+Hoursworked+Occupation+Economicactivity+Distance', data = df, return_type='dataframe')

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns

print(vif)


