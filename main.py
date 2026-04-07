import pandas as pd
from src.data_loader import get_spot_price
from src.vol_surface import build_vol_surface

# Example dummy dataset
data = {
    "strike": [90, 100, 110],
    "maturity": [0.1, 0.1, 0.1],
    "price": [12, 7, 3]
}

df = pd.DataFrame(data)

S = get_spot_price("AAPL")
r = 0.01

df = build_vol_surface(df, S, r)

print(df)
