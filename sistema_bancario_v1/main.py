from user.user import User

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """


def main():
    user = User(0, 500, 3)

    while True:

        option = input(menu).strip()

        if option in ["d", "D"]:
            amount = float(input("Valor do depósito "))
            user.deposit(amount)
        elif option in ["s", "S"]:
            amount = float(input("Valor para saque "))
            user.withdraw(amount)
        elif option in ["e", "E"]:
            statement = user.statement
            print(statement)
        elif option in ["q", "Q"]:
            break

        else:
            print(
                "Operação invalida, por favor seleciona novamente a operação desejada"  # noqa:E501
            )


main()
