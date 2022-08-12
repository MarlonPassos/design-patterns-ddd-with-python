from account import Account
from command import Command


class CreditCommand(Command):
    operation = "credit"

    def __init__(self, account: Account, amount: int):
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.credit(self.amount)
