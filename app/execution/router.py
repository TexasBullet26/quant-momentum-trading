from app.config import settings
from app.execution.paper import PaperBroker
from app.execution.alpaca import AlpacaBroker
from app.execution.coinbase import CoinbaseBroker
class ExecutionRouter:
    def __init__(self,venue='alpaca'):
        if settings.trading_mode=='paper': self.broker=PaperBroker()
        elif venue=='alpaca': self.broker=AlpacaBroker()
        elif venue=='coinbase': self.broker=CoinbaseBroker()
        else: raise ValueError('unsupported venue')
    def market(self,symbol,side,qty):return self.broker.submit_market(symbol,side,qty)
