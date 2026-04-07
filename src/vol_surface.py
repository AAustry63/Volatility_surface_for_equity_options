import pandas as pd
from src.implied_vol import implied_volatility

def build_vol_surface(df, S, r):
    vols = []

    for _, row in df.iterrows():
        iv = implied_volatility(
            C_market=row["price"],
            S=S,
            K=row["strike"],
            T=row["maturity"],
            r=r
        )
        vols.append(iv)

    df["implied_vol"] = vols
    return df
