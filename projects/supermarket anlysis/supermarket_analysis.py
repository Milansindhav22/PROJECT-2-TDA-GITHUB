import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("supermarket_sales.csv")
df['Date'] = pd.to_datetime(df['Date'])

daily_sales = df.groupby('Date')['Total'].sum()

plt.figure()
daily_sales.plot()
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

top_products = df.groupby('Product line')['Quantity'].sum().sort_values(ascending=False)

plt.figure()
top_products.plot(kind='bar')
plt.title("Best-Selling Product Lines")
plt.xlabel("Product Line")
plt.ylabel("Quantity Sold")
plt.show()

gender_sales = df.groupby('Gender')['Total'].sum()

plt.figure()
gender_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Gender")
plt.ylabel("")
plt.show()
