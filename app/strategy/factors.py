import numpy as np
import pandas as pd
def momentum_return(close, lookback, skip=21):
    if len(close)<lookback+skip+1:return np.nan
    return float(close.iloc[-1]/close.iloc[-(lookback+skip+1)]-1)
def trend_strength(close):
    if len(close)<200:return np.nan
    a=close.ewm(span=50,adjust=False).mean().iloc[-1]; b=close.ewm(span=200,adjust=False).mean().iloc[-1]
    return float(a/b-1)
def realized_vol(close,window=20):
    r=np.log(close.astype(float)).diff().dropna()
    return float(r.tail(window).std()*np.sqrt(252)) if len(r)>=window else np.nan
def build_factor_row(df,benchmark_return=None):
    c=df['close'].astype(float); m12=momentum_return(c,252); m6=momentum_return(c,126); m3=momentum_return(c,63); t=trend_strength(c); v=realized_vol(c)
    rs=m12-benchmark_return if benchmark_return is not None and np.isfinite(m12) else np.nan
    return {'m12_1':m12,'m6_1':m6,'m3_1':m3,'relative_strength':rs,'trend_strength':t,'realized_vol':v,'vol_adj_momentum':m12/v if np.isfinite(v) and v>0 else np.nan}
