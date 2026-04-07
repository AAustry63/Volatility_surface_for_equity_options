import numpy as np

def compute_realized_vol(prices):
    returns = np.log(prices / prices.shift(1)).dropna()
    return returns.std() * np.sqrt(252)

def vol_arbitrage_signal(iv, rv, threshold=0.05):
    if iv > rv + threshold:
        return "SELL_VOL"
    elif iv < rv - threshold:
        return "BUY_VOL"
    else:
        return "HOLD"
