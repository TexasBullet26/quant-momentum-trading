from app.config import settings
from app.execution.base import OrderResult
class AlpacaBroker:
    def __init__(self):
        from alpaca.trading.client import TradingClient
        self.client=TradingClient(settings.alpaca_api_key,settings.alpaca_api_secret,paper=settings.alpaca_paper)
    def submit_market(self,symbol,side,qty):
        from alpaca.trading.requests import MarketOrderRequest
        from alpaca.trading.enums import OrderSide,TimeInForce
        req=MarketOrderRequest(symbol=symbol,qty=float(qty),side=OrderSide.BUY if side.lower()=='buy' else OrderSide.SELL,time_in_force=TimeInForce.DAY)
        o=self.client.submit_order(order_data=req)
        return OrderResult('alpaca',symbol,side,float(qty),str(o.status),str(o.id))
