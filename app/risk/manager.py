from dataclasses import dataclass
from app.config import settings
@dataclass
class RiskDecision: allowed: bool; reason: str=''
class RiskManager:
    def __init__(self): self.daily_loss=0.0
    def can_trade(self,symbol,notional,open_positions):
        if notional>settings.max_position_notional:return RiskDecision(False,'hard position cap')
        if self.daily_loss<=-settings.max_daily_loss:return RiskDecision(False,'daily loss limit')
        if open_positions>=settings.max_positions:return RiskDecision(False,'max positions')
        if settings.trading_mode=='live' and not settings.live_trading_enabled:return RiskDecision(False,'live trading disabled')
        return RiskDecision(True,'approved')
