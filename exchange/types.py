from dataclasses import dataclass


@dataclass
class Order:
    id: int
    owner: str
    price: float
    volume: int
    initial_volume: int


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
