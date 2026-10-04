from abc import ABC,abstractmethod
from dataclasses import dataclass
@dataclass
class OrderResult: broker:str; symbol:str; side:str; qty:float; status:str; order_id:str=''
class Broker(ABC):
    @abstractmethod
    def submit_market(self,symbol,side,qty): raise NotImplementedError
