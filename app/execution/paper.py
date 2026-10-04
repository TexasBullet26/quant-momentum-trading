import uuid
from app.execution.base import Broker,OrderResult
class PaperBroker(Broker):
    def __init__(self):self.orders=[]
    def submit_market(self,symbol,side,qty):
        o=OrderResult('paper',symbol,side,float(qty),'filled',str(uuid.uuid4())); self.orders.append(o); return o
