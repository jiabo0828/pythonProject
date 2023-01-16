
import pandas as pd

df = pd.concat(
    map(pd.read_csv, ['/Users/jiabozhu/Desktop/pricehouse.csv',
                      '/Users/jiabozhu/Desktop/lsoa_airbnb.csv']), ignore_index=True)
df.head()
df.to_csv('/Users/jiabozhu/Desktop/18.csv')















