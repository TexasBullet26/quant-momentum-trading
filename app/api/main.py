from fastapi import FastAPI
from app.config import settings
app=FastAPI(title='Quant Momentum V3',version='3.0.0')
@app.get('/health')
def health():return {'status':'ok','version':'3.0.0'}
@app.get('/config')
def config():return {'trading_mode':settings.trading_mode,'live_trading_enabled':settings.live_trading_enabled,'max_position_notional':settings.max_position_notional,'max_daily_loss':settings.max_daily_loss,'max_positions':settings.max_positions}
