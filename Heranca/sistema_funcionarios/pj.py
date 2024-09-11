from funcionario import Funcionario

class FuncionarioPJ(Funcionario):
    def calcular_pagamento(self):
        print(f"O salário de {self.nome} (PJ) é: R$ {self.salario_base:.2f}")