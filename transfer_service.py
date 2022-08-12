from account import Account


class TransferService:
    def transfer(self, account_from: Account, account_to: Account, amount: int):
        account_from.debit(amount)
        account_to.credit(amount)
