class SaldoInsuficienteError(Exception):
    pass


class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")

        self.saldo -= valor
        print(f"Saque realizado com sucesso!")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


conta = ContaBancaria(500)

try:
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    conta.sacar(valor_saque)

except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")