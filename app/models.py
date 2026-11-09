from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str


@dataclass
class Order:
    id: int
    user_id: int
    email: str
    total: float