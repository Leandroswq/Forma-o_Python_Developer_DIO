class User:
    def __init__(self, account) -> None:
        self.account = account


if __name__ == "__main__":
    from sistema_bancario_v2.account.checking_account import CheckingAccount

    account = CheckingAccount(500, 300, 3)
    user = User(account)
    user.account.deposit(300)
    user.account.withdraw(amount=200)
    print(user.account.balance, user.account.statement, sep="\n")
