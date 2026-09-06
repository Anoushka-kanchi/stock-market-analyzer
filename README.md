# 📈 Stock Market Analyzer

A Python-based stock market analysis project built progressively
using Python, Pandas, NumPy, data visualization, APIs, and web development.

## 🚧 Project Status

**Phase 1 completed ✅**
**Phase 2 completed ✅**

Currently preparing for **Phase 3 — Backend**

### Phase 1 — Data Analysis
### Phase 1 — Data Analysis

- [x] Load stock data
- [x] Explore the dataset
- [x] Clean and inspect the data
- [x] Calculate basic statistics
- [x] Calculate total return
- [x] Calculate daily returns
- [x] Calculate moving averages
- [x] Analyze volatility
- [x] Create stock visualizations
- [x] Generate stock analysis report

### Phase 2 — Market Data API
- [ ] Connect to a stock market API
- [ ] Fetch historical/live data
- [ ] Handle API responses

### Phase 3 — Backend
- [ ] Build backend using Flask/Django
- [ ] Create API endpoints
- [ ] Connect database

### Phase 4 — Frontend
- [ ] Build stock dashboard
- [ ] Add interactive charts
- [ ] Add stock comparison

### Phase 5 — Natural Language / AI
- [ ] Allow users to ask questions about stocks
- [ ] Analyze questions using stock data
- [ ] Generate natural-language responses

---

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- APIs
- Flask / Django
- SQL
- HTML / CSS / JavaScript
- AI / LLM APIs

---

## 📚 What I'm Learning

This project is being built phase by phase to understand
Python, data analysis, APIs, backend development, and
eventually AI-powered data analysis.


## Phase 2 — API-Based Stock Analysis

In Phase 2, the project was upgraded to fetch real stock-market data using the Alpha Vantage API.

### Features

- Fetches stock data using a stock symbol
- Converts API JSON data into a Pandas DataFrame
- Calculates basic statistics, returns, volatility, and moving averages
- Performs basic trend analysis
- Visualizes closing prices and moving averages using Matplotlib
- Saves analyzed stock data as CSV files
- Uses `.env` to securely store the API key

### How to Run

```bash
cd phase-2-api/src
python api.py