from app.risk.manager import RiskManager
from app.config import settings
def test_position_cap():assert not RiskManager().can_trade('AAPL',settings.max_position_notional+1,0).allowed
