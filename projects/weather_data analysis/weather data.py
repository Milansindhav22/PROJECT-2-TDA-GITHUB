import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/weather_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

plt.figure()
plt.plot(df['Date'], df['AvgTemp'])
plt.title("Average Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

seasonal_temp = df.groupby('Month')['AvgTemp'].mean()

plt.figure()
seasonal_temp.plot(kind='bar')
plt.title("Seasonal Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

plt.figure()
sns.histplot(df['Rainfall'], bins=20)
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall (mm)")
plt.show()
extreme_temp = df[df['MaxTemp'] > 40]
extreme_rain = df[df['Rainfall'] > 100]

print("Extreme Temperature Days:", extreme_temp.shape[0])
print("Extreme Rainfall Days:", extreme_rain.shape[0])
