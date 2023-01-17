import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jiabozhu/Desktop/autotimewestnew.csv', index_col = u'TIME')

df['Westminster'].plot(label='Westminster', color='orange')
df['cityoflondon'].plot(label='cityoflondon',color='blue')
df['KensingtonandChelsea'].plot(label='KensingtonandChelsea', color='red')
df['HammersmithandFulham'].plot(label='HammersmithandFulham',color='green')
df['Southwark'].plot(label='Southwark',color='pink')
df['TowerHamlets'].plot(label='TowerHamlets', color='cyan')
df['Hackney'].plot(label='Hackney',color='magenta')
df['Islington'].plot(label='Islington',color='yellow')
df['Camden'].plot(label='Camden', color='brown')
df['Lambeth'].plot(label='Lambeth', color='gray')
df['alllondon'].plot(label='alllondon',color='black')


plt.xlabel("TIME")
plt.ylabel("VALUE")
plt.legend(labels=['Westminster',
                   'cityoflondon',
                   'KensingtonandChelsea',
                   'HammersmithandFulham',
                   'Southwark',
                   'TowerHamlets',
                   'Hackney',
                   'Islington',
                   'Camden',
                   'Lambeth',
                   'alllondon'],loc='best')
plt.title('Airbnb distribution density by borough of Inner London(2016-2022)',size=14)
plt.grid(True)
plt.show()
