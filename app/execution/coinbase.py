from app.config import settings
class CoinbaseBroker:
    def __init__(self):
        from coinbase.rest import RESTClient
        self.client=RESTClient(api_key=settings.coinbase_api_key,api_secret=settings.coinbase_api_secret)
    def submit_market(self,symbol,side,qty):
        raise NotImplementedError('Implement product-specific Coinbase Advanced Trade order mapping after confirming product/order schema for the target account.')
