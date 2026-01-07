import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_data.csv")
df['Daily Return'] = df['Close'].pct_change()

plt.plot(df['Date'], df['Close'])
plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
