import numpy as np,pandas as pd
from app.strategy.factors import momentum_return,realized_vol
def test_momentum():
 s=pd.Series(np.arange(300,dtype=float)+100);assert np.isfinite(momentum_return(s,252))
def test_vol():
 s=pd.Series(100*np.exp(np.cumsum(np.random.default_rng(1).normal(0,.01,300))));assert realized_vol(s)>0
