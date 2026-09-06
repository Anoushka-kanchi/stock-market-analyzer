# 📚 Learning Notes

## Phase 1 — Data Analysis

### Stock Market Basics

- **Date:** Date of the trading session.
- **Open:** Price at which the stock started trading that day.
- **High:** Highest price reached during that trading session.
- **Low:** Lowest price reached during that trading session.
- **Close:** Price at which the stock ended trading that day.
- **Volume:** Number of shares traded during the session.
- **Total Return:** Overall percentage change from the first closing price to the last closing price.
- **Daily Return:** Percentage change in the closing price from one trading day to the next.
- **Volatility:** Measure of how much daily returns fluctuate.
- **Moving Average:** Average price calculated over a specific number of previous trading days.
- **Basic Trend Analysis:** Comparing the current price with a moving average to identify a simple upward or downward trend.

### Python

- Variables
- `if / else` conditions
- Arithmetic operations
- Conditional expressions
- Printing formatted output
- Working with external libraries using `import`

### Pandas

- `pd.read_csv()` — Read CSV data into a DataFrame
- `df.head()` — View first rows
- `df.tail()` — View last rows
- `df.shape` — Get number of rows and columns
- `df.info()` — Inspect columns and data types
- `df.describe()` — Get statistical summary
- `df["Column"]` — Select a column
- `.max()` — Find maximum value
- `.min()` — Find minimum value
- `.mean()` — Calculate average
- `.iloc[]` — Access values by position
- `.shift()` — Shift values between rows
- `.rolling()` — Create a moving window
- `.std()` — Calculate standard deviation

### NumPy

Coming soon...

### Matplotlib

- `plt.plot()` — Create a line plot
- `plt.xlabel()` — Label the X-axis
- `plt.ylabel()` — Label the Y-axis
- `plt.title()` — Add a chart title
- `plt.legend()` — Display the legend
- `plt.xticks()` — Customize X-axis tick labels
- `plt.tight_layout()` — Adjust the layout
- `plt.show()` — Display the chart

### Data Visualization

- Line charts
- Plotting multiple data series
- X-axis and Y-axis labels
- Chart titles
- Legends

## Phase 2 — Working with APIs
### APIs

An API (Application Programming Interface) allows one software application to communicate with another.

In this project, I use the Alpha Vantage API to request real stock-market data instead of reading it from a manually downloaded CSV file.

The basic flow is:

User → API Request → Alpha Vantage → JSON Response → Pandas DataFrame
### JSON

JSON (JavaScript Object Notation) is a common format used to exchange data between applications.

The Alpha Vantage API sends the stock data as a JSON response.

The response contains information such as:

- Stock metadata
- Date
- Open price
- High price
- Low price
- Close price
- Trading volume

I use Python to extract the required stock data from the JSON response and then convert it into a Pandas DataFrame for analysis.