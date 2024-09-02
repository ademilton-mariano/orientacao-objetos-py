# Criando a classe ContaBancaria 
class ContaBancaria:
    
    # construtor da classe
    def __init__(self, nome_do_titular, saldo=0):
        self.nome_do_titular = nome_do_titular
        self.saldo = saldo

    # método para depositar um valor na conta
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    # método para sacar um valor da conta
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    # método para consultar o saldo da conta
    def consultar_saldo(self):
        return self.saldo
