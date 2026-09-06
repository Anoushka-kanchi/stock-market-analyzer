import requests
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from analyzer import (
    calculate_basic_statistics,
    calculate_return,
    calculate_volatility,
    calculate_moving_average,
    determine_trend
)
from config import API_KEY
def main():
    url = "https://www.alphavantage.co/query"

    while True:
        symbol = input("Enter stock symbol: ").strip().upper()

        if symbol:
            break

        print("Please enter a stock symbol.")
    while True:
        try:
            days = int(input("Enter number of trading days: "))

            if days < 3:
                print("Please enter at least 3 trading days.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException:
        print("Unable to connect to the stock market API.")
        exit()

    #print(data.keys())
    if "Time Series (Daily)" in data:
        daily_data = data["Time Series (Daily)"]
    else:
        if "Note" in data:
            print("API request limit reached. Please try again later.")
        elif "Error Message" in data:
            print("Invalid stock symbol. Please check the symbol and try again.")
        else:
            print("Unable to retrieve stock data.")
        exit()
    df = pd.DataFrame.from_dict(daily_data, orient="index")

    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    df.index.name='Date'
    df=df.reset_index()

    df["Date"] = pd.to_datetime(df["Date"])
    numeric_columns = ["Open", "High", "Low", "Close", "Volume"]

    df[numeric_columns] = df[numeric_columns].astype(float)
    df = df.sort_values("Date")
    df = df.iloc[-days:]

    highest_close, lowest_close, average_close = calculate_basic_statistics(df)

    price_change, return_percentage = calculate_return(df)

    volatility = calculate_volatility(df)

    df = calculate_moving_average(df)

    trend = determine_trend(df)

    data_folder = Path(__file__).resolve().parent.parent / "data"
    data_folder.mkdir(exist_ok=True)

    df.to_csv(data_folder / f"{symbol}_stock_data.csv", index=False)

    print("\n📊 STOCK ANALYSIS REPORT")
    print("------------------------")

    print("Stock:", symbol)
    print("Highest Closing Price:", round(highest_close, 2))
    print("Lowest Closing Price:", round(lowest_close, 2))
    print("Average Closing Price:", round(average_close, 2))
    print("Total Return:", round(return_percentage, 2), "%")
    print("Daily Volatility:", round(volatility, 2), "%")
    print("Current Trend:", trend)

    plt.plot(df["Date"], df["Close"], label="Closing Price")

    plt.plot(df["Date"], df["MA_3"], label="3-Day Moving Average")
    #chart
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{symbol} Stock Price")

    plt.xticks(rotation=45)

    plt.legend()

    plt.show()
if __name__ == "__main__":
    main()