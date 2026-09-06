import pandas as pd
def calculate_basic_statistics(df):

    highest_close = df["Close"].max()
    lowest_close = df["Close"].min()
    average_close = df["Close"].mean()

    return highest_close, lowest_close, average_close

def calculate_return(df):

    first_close = df["Close"].iloc[0]
    last_close = df["Close"].iloc[-1]

    price_change = last_close - first_close

    return_percentage = (price_change / first_close) * 100

    return price_change, return_percentage

def calculate_volatility(df):

    df["Daily_Return"] = df["Close"].pct_change() * 100

    volatility = df["Daily_Return"].std()

    return volatility

def calculate_moving_average(df):

    df["MA_3"] = df["Close"].rolling(3).mean()

    return df

def determine_trend(df):

    latest_close = df["Close"].iloc[-1]
    latest_ma = df["MA_3"].iloc[-1]

    if pd.isna(latest_ma):
        return "Not enough data"

    if latest_close > latest_ma:
        return "Upward"
    else:
        return "Downward"