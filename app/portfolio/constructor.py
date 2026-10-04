import pandas as pd
def volatility_scaled_weights(scores,max_positions=10,max_weight=.10):
    x=scores.dropna(subset=['momentum_score','realized_vol']); x=x[x.momentum_score>0].head(max_positions)
    if x.empty:return pd.Series(dtype=float)
    w=(x.momentum_score/x.realized_vol.clip(lower=.05)); w=w/w.sum(); w=w.clip(upper=max_weight); return w/w.sum()
def target_notional(weights,equity,max_position_notional=250):return (weights*equity).clip(upper=max_position_notional)
