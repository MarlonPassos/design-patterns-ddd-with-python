from dataclasses import dataclass


@dataclass
class Transaction:
    ttype: str
    amount: int
