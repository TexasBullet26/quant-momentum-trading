import pandas as pd
from app.backtest.engine import run_single_asset
def test_no_lookahead():
 df=pd.DataFrame({'date':pd.bdate_range('2025-01-01',periods=5),'close':[100,110,100,110,100]});signal=pd.Series([0,1,0,0,0]);out=run_single_asset(df,signal,commission_bps=0,slippage_bps=0);assert out.loc[1,'strategy_ret']==0
