import numpy as np
import pandas as pd
def max_drawdown(equity):return float((equity/equity.cummax()-1).min())
def run_single_asset(df,signal,initial_cash=10000,commission_bps=1,slippage_bps=5):
    d=df.sort_values('date').reset_index(drop=True).copy(); d['signal']=signal.reindex(d.index).fillna(0); d['ret']=d.close.pct_change().fillna(0)
    d['strategy_ret']=d.signal.shift(1).fillna(0)*d.ret; turnover=d.signal.diff().abs().fillna(d.signal.abs()); d['net_ret']=d.strategy_ret-turnover*(commission_bps+slippage_bps)/10000; d['equity']=initial_cash*(1+d.net_ret).cumprod(); return d
def performance_summary(result):
    r=result.net_ret; years=max(len(r)/252,1/252); cagr=(result.equity.iloc[-1]/result.equity.iloc[0])**(1/years)-1; sharpe=r.mean()/r.std()*np.sqrt(252) if r.std() else 0; down=r[r<0].std(); sortino=r.mean()/down*np.sqrt(252) if down else 0
    return {'final_equity':float(result.equity.iloc[-1]),'CAGR':float(cagr),'Sharpe':float(sharpe),'Sortino':float(sortino),'MaxDrawdown':max_drawdown(result.equity)}
