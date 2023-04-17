import pandas as pd
import matplotlib.pyplot as plt

headers = ['Time', 'Temperature', 'Humidity', 'Pressure']

df = pd.read_csv('20220213115410_data.csv', header=0)
print(df)
print(df['Pressure'])

ax = df.plot(x ="Time", y=['Temperature', 'Humidity'], kind='line', grid=True)
ax.set_ylabel('°C / %rel')
ax = df['Pressure'].plot(secondary_y=True, color='k', kind='line')
ax.set_ylabel('Pascal')


plt.show()
