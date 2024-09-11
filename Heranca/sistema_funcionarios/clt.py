from funcionario import Funcionario

class FuncionarioCLT(Funcionario):
    def calcular_pagamento(self):
        salario_liquido = self.salario_base * 0.92  # 8% de desconto do INSS
        print(f"O salário de {self.nome} (CLT) é: R$ {salario_liquido:.2f}")