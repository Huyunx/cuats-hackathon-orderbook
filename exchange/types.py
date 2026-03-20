from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    id: int
    owner: str
    price: float
    volume: int
    initial_volume: int
    time: datetime

    def __init__(self, id: int, owner: str, price: float, volume: int):
        self.id = id
        self.owner = owner
        self.price = price
        self.volume = volume
        self.time = datetime.now()
        self.initial_volume = volume

    def __lt__(self, other):
        if self.price == other.price:
            return self.time < other.time
        return self.price < other.price


@dataclass
class Trade:
    id: int
    buyer: str
    seller: str
    price: float
    volume: int


@dataclass
class OrderResult:
    average_price: float
    filled_volume: int
    remaining_volume: int


@dataclass
class OrderStatus:
    price: float
    filled_volume: int
    remaining_volume: int
