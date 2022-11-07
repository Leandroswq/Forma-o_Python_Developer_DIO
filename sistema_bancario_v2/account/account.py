class Account:
    def __init__(
        self, balance: float, account_number, branch: str = 1
    ) -> None:
        self.__balance = balance
        self.__statement = []
        self.__branch = branch
        self.__account_number = account_number

    @property
    def branch(self):
        return f"{self.__branch:04}"

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        self.__balance = value

    @property
    def statement(self):
        if len(self.__statement) > 0:
            statement_strings = [
                f"tipo: {s['type']} Valor: {s['amount']} Total: {s['total']}"
                for s in self.__statement
            ]
            statements = "\n".join(statement_strings)
            return f"Operações: \n{statements} \nSaldo total: {self.balance}"

        return "Não foram realizadas movimentações"

    def format(self, value: float):
        return f"R$ {value:.2f}"

    def __add_statement__(
        self, type: str, /, *, amount: float
    ):  # positional only and keyword only
        statement = {
            "type": type,
            "amount": self.format(amount),
            "total": self.format(self.__balance),
        }

        self.__statement.append(statement)

    def deposit(self, amount: float, /) -> None:  # positional only
        if amount <= 0:
            return print(
                "Operação inválida, o deposito precisa de um valor positivo"
            )
        self.__balance += amount
        self.__add_statement__("Deposito", amount=amount)

    def withdraw(self, *, amount: float) -> None:  # keyword only
        if self.__balance < amount:
            return print("Saldo insuficiente")
        self.__balance -= amount
        self.__add_statement__("Saque", amount=amount)
