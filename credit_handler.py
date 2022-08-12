from command import Command
from observer import Observer


class CreditHandler(Observer):
    operation = "credit"

    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def notify(self, command: Command) -> None:
        account = self.account_repository.get(command.document)
        if account:
            account.credit(command.amount)
