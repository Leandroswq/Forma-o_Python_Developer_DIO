from sistema_bancario_v2.account.account import Account


class CheckingAccount(Account):
    def __init__(
        self,
        balance: float,
        withdraw_limit: float,
        withdraw_qtd_limit: int = 3,
    ) -> None:
        Account.__init__(self, balance)
        self.__withdraw_qtd = 0
        self.__WITHDRAW_QTD_LIMIT = withdraw_qtd_limit
        self.__WITHDRAW_LIMIT = withdraw_limit

    def withdraw(self, *, amount: float) -> None:  # keyword only
        if self.__withdraw_qtd >= self.__WITHDRAW_QTD_LIMIT:
            return print("Operação negada, limite de saque atingido")
        if amount > self.__WITHDRAW_LIMIT:
            return print("Operação negada, o limite de saque é R$ 500.00")
        if self.balance < amount:
            return print("Saldo insuficiente")
        self.balance -= amount
        self.__withdraw_qtd += 1
        self.__add_statement__("Saque", amount=amount)


if __name__ == "__main__":
    Account = CheckingAccount(500, 500)
    Account.deposit(300)
    Account.withdraw(amount=200)
    print(Account.balance, Account.statement, sep="\n")
