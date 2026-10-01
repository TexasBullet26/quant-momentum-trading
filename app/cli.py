import argparse,pandas as pd
from app.strategy.momentum import build_universe_factor_table
from app.portfolio.constructor import volatility_scaled_weights
def main():
 p=argparse.ArgumentParser();p.add_argument('--csv',required=True);a=p.parse_args();df=pd.read_csv(a.csv,parse_dates=['date']);history={s:g.sort_values('date') for s,g in df.groupby('symbol')};scores=build_universe_factor_table(history);print(scores[['momentum_score','m12_1','m6_1','m3_1','realized_vol']].head(20));print('\nTarget weights:\n',volatility_scaled_weights(scores))
if __name__=='__main__':main()
