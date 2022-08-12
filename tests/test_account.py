from account import AccountBuilder
from credit_command import CreditCommand
from debit_command import DebitCommand
from transfer_command import TransferCommand
from transfer_service import TransferService


def test_should_create_an_account():
    account = AccountBuilder("1111-111-111-11") \
        .set_bank("003") \
        .set_branch("0001") \
        .set_account("0003").build()

    assert account.get_balance() == 0


def test_should_create_an_account_and_make_deposit():
    account = AccountBuilder("1111-111-111-11") \
        .set_bank("003") \
        .set_branch("0001") \
        .set_account("0003").build()
    credit_command = CreditCommand(account, 1000)
    credit_command.execute()

    assert account.get_balance() == 1000


def test_should_create_an_account_and_make_debit():
    account = AccountBuilder("1111-111-111-11") \
        .set_bank("003") \
        .set_branch("0001") \
        .set_account("0003").build()

    credit_command = CreditCommand(account, 1000)
    credit_command.execute()

    debit_command = DebitCommand(account, 500)
    debit_command.execute()

    assert account.get_balance() == 500


def test_must_create_two_accounts_and_a_transfer():
    account_from = AccountBuilder("1111-111-111-11") \
        .set_bank("003") \
        .set_branch("0001") \
        .set_account("0003").build()

    account_to = AccountBuilder("2222-222-222-22") \
        .set_bank("003") \
        .set_branch("0001") \
        .set_account("0003").build()

    credit_command = CreditCommand(account_from, 1000)
    credit_command.execute()

    credit_command = CreditCommand(account_to, 500)
    credit_command.execute()

    transfer_command = TransferCommand(account_from, account_to, 700)
    transfer_command.execute()

    assert account_from.get_balance() == 300
    assert account_to.get_balance() == 1200
