from veiculo_passeio import VeiculoPasseio

class Carro(VeiculoPasseio):
    def __init__(self, numRodas, combustivel, velocidade, cor, tipo, capacPassageiros, numPortas):
        super().__init__(numRodas, combustivel, velocidade, cor, tipo, capacPassageiros)
        self.numPortas = numPortas

    def __str__(self):
        return f"{super().__str__()}\nNúmero de portas: {self.numPortas}"