import requests
import pandas as pd
from app.config import settings
class MassiveClient:
    def __init__(self, api_key=None, base_url=None):
        self.api_key = api_key or settings.massive_api_key
        self.base_url = (base_url or settings.massive_base_url).rstrip('/')
    def daily_bars(self, symbol, start, end):
        url=f'{self.base_url}/v2/aggs/ticker/{symbol}/range/1/day/{start}/{end}'
        r=requests.get(url,params={'adjusted':'true','sort':'asc','limit':50000},headers={'Authorization':f'Bearer {self.api_key}'},timeout=30)
        r.raise_for_status(); rows=r.json().get('results',[])
        if not rows: return pd.DataFrame(columns=['date','symbol','open','high','low','close','volume'])
        df=pd.DataFrame(rows); df['date']=pd.to_datetime(df['t'],unit='ms',utc=True).dt.tz_convert(None); df['symbol']=symbol
        return df.rename(columns={'o':'open','h':'high','l':'low','c':'close','v':'volume'})[['date','symbol','open','high','low','close','volume']]
