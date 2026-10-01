import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
class Settings(BaseModel):
    trading_mode: str = Field(default_factory=lambda: os.getenv('TRADING_MODE','paper'))
    live_trading_enabled: bool = Field(default_factory=lambda: os.getenv('LIVE_TRADING_ENABLED','false').lower()=='true')
    max_position_notional: float = Field(default_factory=lambda: float(os.getenv('MAX_POSITION_NOTIONAL','250')))
    max_daily_loss: float = Field(default_factory=lambda: float(os.getenv('MAX_DAILY_LOSS','50')))
    max_positions: int = Field(default_factory=lambda: int(os.getenv('MAX_POSITIONS','10')))
    commission_bps: float = Field(default_factory=lambda: float(os.getenv('COMMISSION_BPS','1')))
    slippage_bps: float = Field(default_factory=lambda: float(os.getenv('SLIPPAGE_BPS','5')))
    massive_api_key: str = Field(default_factory=lambda: os.getenv('MASSIVE_API_KEY',''))
    massive_base_url: str = Field(default_factory=lambda: os.getenv('MASSIVE_BASE_URL','https://api.massive.com'))
    alpaca_api_key: str = Field(default_factory=lambda: os.getenv('ALPACA_API_KEY',''))
    alpaca_api_secret: str = Field(default_factory=lambda: os.getenv('ALPACA_API_SECRET',''))
    alpaca_paper: bool = Field(default_factory=lambda: os.getenv('ALPACA_PAPER','true').lower()=='true')
    coinbase_api_key: str = Field(default_factory=lambda: os.getenv('COINBASE_API_KEY',''))
    coinbase_api_secret: str = Field(default_factory=lambda: os.getenv('COINBASE_API_SECRET',''))
settings = Settings()
