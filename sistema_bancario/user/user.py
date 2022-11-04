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
        statement_strings = [
            f"tipo: {s['type']} Valor: {s['amount']} Total: {s['total']}"
            for s in self.__statement
        ]
        return "\n".join(statement_strings)

    def format(self, value: float):
        return f"R$ {value:.2f}"

    def __add_statement__(self, type: str, amount: float):
        statement = {
            "type": type,
            "amount": self.format(amount),
            "total": self.format(self.__balance),
        }

        self.__statement.append(statement)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            return print(
                "Operação inválida, o deposito precisa de um valor positivo"
            )
        self.__balance += amount
        self.__add_statement__("Deposito", amount)

    def withdraw(self, amount: float) -> None:
        if self.__withdraw_qtd >= self.__WITHDRAW_QTD_LIMIT:
            return print("Operação negada, limite de saque atingido")
        if amount > self.__WITHDRAW_LIMIT:
            return print("Operação negada, o limite de saque é R$ 500.00")
        if self.__balance < amount:
            return print("Saldo insuficiente")
        self.__balance -= amount
        self.__add_statement__("Saque", amount)


if __name__ == "__main__":
    user = User(500, 300, 3)
    user.deposit(300)
    user.withdraw(200)
    print(user.balance, user.statement, sep="\n")
