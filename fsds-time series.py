import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jiabozhu/Desktop/autotimewestnew.csv', index_col = u'TIME')

df['Westminsterairbnbper'].plot(label='Westminsterairbnbper', color='orange')
df['londoncityairbnbper'].plot(label='londoncityairbnbper',color='blue')
df['alllondonairbnbper'].plot(label='alllondonairbnbper',color='black')


plt.figure(figsize=(30, 10))
plt.xlabel("TIME")
plt.ylabel("VALUE")
plt.title('Westminsterairbnbper vs Camdenairbnbper vs alllondonairbnbper(2016-2021)',size=22)
plt.grid(True)
plt.show()