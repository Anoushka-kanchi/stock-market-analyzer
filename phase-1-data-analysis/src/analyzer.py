import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("../data/stock_data.csv")

#print(df.head())
#print(df.info())
#print(df.shape)
#print(df.describe())
#print(df["Close"])

highest_close = df["Close"].max()
lowest_close = df["Close"].min()
average_close = df["Close"].mean()



first_close = df["Close"].iloc[0]
last_close = df["Close"].iloc[-1]
price_change=last_close-first_close
return_percentage = (price_change/first_close)*100
df["Previous_Close"] = df["Close"].shift(1)
df["Daily_Return"] = ((df["Close"] - df["Previous_Close"]) / df["Previous_Close"]) * 100
average_daily_return = df["Daily_Return"].mean()
volatility = df["Daily_Return"].std()
df["MA_3"] = df["Close"].rolling(3).mean()
latest_close = df["Close"].iloc[-1]
latest_ma = df["MA_3"].iloc[-1]


print()
print("\n📊 STOCK ANALYSIS REPORT")
print("------------------------")
print("Highest Closing Price:", highest_close)
print("Lowest Closing Price:", lowest_close)
print("Average Closing Price:", round(average_close, 2))
print("Total Return:", round(return_percentage, 2), "%")
print("Daily Volatility:", round(volatility, 2), "%")
print("Current Trend:", "Upward" if latest_close > latest_ma else "Downward")

plt.plot(df["Date"], df["Close"], label="Closing Price")
plt.plot(df["Date"], df["MA_3"], label="3-Day Moving Average")

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stock Price Analysis")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()