from scipy.optimize import brentq
from src.black_scholes import black_scholes_call

def implied_volatility(C_market, S, K, T, r):
    def objective(sigma):
        return black_scholes_call(S, K, T, r, sigma) - C_market

    try:
        return brentq(objective, 1e-6, 5.0)
    except:
        return None
