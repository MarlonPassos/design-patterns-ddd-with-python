from account import Account
from command import Command


class DebitCommand(Command):
    operation = "debit"

    def __init__(self, account: Account, amount: int):
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.debit(self.amount)
