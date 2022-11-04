class User:
    def __init__(self, balance: float, limit: float) -> None:
        self.__balance = balance
        self.__limit = limit
        self.__statement = []

        self.__withdraw_qtd__ = 0
        self.__WITHDRAW_QTD_LIMIT__ = 3

    @property
    def balance(self):
        return self.__balance

    @property
    def statement(self):
        return self.__statement


if __name__ == "__main__":
    user = User(500, 300)
    user.Deposit(300)
    print(user.balance, user.statement)
