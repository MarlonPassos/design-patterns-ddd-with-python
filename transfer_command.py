from account import Account
from command import Command
from transfer_service import TransferService


class TransferCommand(Command):
    operation = "transfer"

    def __init__(self, account_from: Account, account_to: Account, amount: int):
        self.account_from = account_from
        self.account_to = account_to
        self.amount = amount

    def execute(self) -> None:
        transfer_service = TransferService()
        transfer_service.transfer(self.account_from, self.account_to, self.amount)
