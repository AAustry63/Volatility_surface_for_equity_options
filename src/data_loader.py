import yfinance as yf

def get_spot_price(ticker="AAPL"):
    data = yf.Ticker(ticker)
    return data.history(period="1d")["Close"].iloc[-1]
