from sistema_bancario_v2.account.account import Account
from typing import List


class User:
    def __init__(self, cpf: str, address: str, account: List[Account]) -> None:
        self.__cpf = "".join([digit for digit in cpf if digit.isdigit()])
        self.__address = address
        self.__account = account

    @property
    def cpf(self):
        return self.__cpf

    @property
    def address(self):
        return self.__address

    @property
    def account(self):
        return self.__account

    def add_account(self, account: Account):
        self.__account.append(account)


if __name__ == "__main__":
    from sistema_bancario_v2.account.checking_account import CheckingAccount

    account = CheckingAccount(500, 500, 3, withdraw_qtd_limit=5, branch=2)
    user = User("5d@d5", "ddd", [account])
    user.account[0].deposit(300)
    user.account[0].withdraw(amount=200)
    print(
        user.account[0].balance,
        user.account[0].statement,
        user.account[0].branch,
        user.account[0].account_number,
        sep="\n",
    )
    print(user.cpf, user.address)
