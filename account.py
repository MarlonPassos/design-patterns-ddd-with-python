from typing import List

from transaction import Transaction


class Account:
    def __init__(self, account_builder: "AccountBuilder"):
        self._bank = account_builder.bank
        self._branch = account_builder.branch
        self._account = account_builder.account
        self._document = account_builder.document
        self.transactions: List[Transaction] = []
        self.balance = 0

    def credit(self, amount: int):
        self.transactions.append(Transaction("credit", amount))

    def debit(self, amount: int):
        self.transactions.append(Transaction("debit", amount))

    def get_balance(self):
        for transaction in self.transactions:
            if transaction.ttype == "credit":
                self.balance += transaction.amount
            elif transaction.ttype == "debit":
                self.balance -= transaction.amount

        return self.balance


class AccountBuilder:
    bank: str
    branch: str
    account: str
    document: str

    def __init__(self, document: str):
        self.document = document

    def set_bank(self, bank: str):
        self.bank = bank
        return self

    def set_branch(self, branch: str):
        self.branch = branch
        return self

    def set_account(self, account: str):
        self.account = account
        return self

    def build(self) -> Account:
        account = Account(self)
        return account
