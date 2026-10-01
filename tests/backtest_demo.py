import numpy as np,pandas as pd
from app.backtest.engine import run_single_asset,performance_summary
rng=np.random.default_rng(42);n=800;dates=pd.bdate_range('2023-01-02',periods=n);returns=rng.normal(.0003,.012,n);close=100*np.cumprod(1+returns);df=pd.DataFrame({'date':dates,'close':close});s=pd.Series(close);signal=(s.rolling(100).mean()>s.rolling(200).mean()).astype(int);r=run_single_asset(df,signal);print(performance_summary(r));r.to_csv('backtest_result.csv',index=False)
