class User:
    def __init__(
        self,
        balance: float,
        withdraw_limit: float,
        withdraw_qtd_limit: int = 3,
    ) -> None:
        self.__balance = balance
        self.__statement = []

        self.__WITHDRAW_LIMIT = withdraw_limit
        self.__withdraw_qtd = 0
        self.__WITHDRAW_QTD_LIMIT = withdraw_qtd_limit

    @property
    def balance(self):
        return self.__balance

    @property
    def statement(self):
        return self.__statement

    def __add_statement__(self, type: str, amount: float):
        statement = {
            "type": type,
            "amount": f"{amount:.2f}",
            "total": f"{self.__balance:.2f}",
        }

        self.__statement.append(statement)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            return print("Deposit needs a positive amount")
        self.__balance += amount
        self.__add_statement__("Deposit", amount)
        print(self.__balance)

    def withdraw(self, amount: float) -> None:
        if self.__withdraw_qtd >= 3:
            return print("Daily withdrawal limit reached, transaction denied")
        if amount > 500:
            return print("The maximum withdrawal allowed is R$ 500.00")
        if self.__balance < amount:
            return print("insufficient funds")
        self.__balance -= amount
        self.__add_statement__("Withdraw", amount)


if __name__ == "__main__":
    user = User(500, 300, 3)
    user.deposit(300)
    user.withdraw(200)
    print(user.balance, user.statement)
