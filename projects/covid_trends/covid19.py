import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/covid_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

plt.plot(df['Date'], df['Confirmed'], label='Confirmed')
plt.plot(df['Date'], df['Recovered'], label='Recovered')
plt.plot(df['Date'], df['Deaths'], label='Deaths')
plt.legend()
plt.title("COVID-19 Trends")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.show()
