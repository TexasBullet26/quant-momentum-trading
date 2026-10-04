import numpy as np
import pandas as pd
from app.strategy.factors import build_factor_row
WEIGHTS={'m12_1':.35,'m6_1':.25,'m3_1':.15,'relative_strength':.10,'trend_strength':.10,'vol_adj_momentum':.05}
def z(s):
    s=s.replace([np.inf,-np.inf],np.nan).fillna(0); sd=s.std(ddof=0)
    return pd.Series(0.0,index=s.index) if not np.isfinite(sd) or sd==0 else (s-s.mean())/sd
def score_universe(factors):
    x=factors.copy()
    for c in WEIGHTS:x['z_'+c]=z(x[c])
    x['momentum_score']=sum(w*x['z_'+c] for c,w in WEIGHTS.items())
    return x.sort_values('momentum_score',ascending=False)
def build_universe_factor_table(history,benchmark=None):
    br=build_factor_row(benchmark)['m12_1'] if benchmark is not None else None; rows=[]
    for sym,df in history.items():
        if len(df)>=260:
            r=build_factor_row(df,br); r['symbol']=sym; rows.append(r)
    return score_universe(pd.DataFrame(rows).set_index('symbol')) if rows else pd.DataFrame()
