from veiculo import Veiculo

class VeiculoPasseio(Veiculo):
    def __init__(self, numRodas, combustivel, velocidade, cor, tipo, capacPassageiros):
        super().__init__(numRodas, combustivel, velocidade, cor, tipo)
        self.capacPassageiros = capacPassageiros

    def __str__(self):
        return f"{super().__str__()}\nCapacidade de pessoas: {self.capacPassageiros}"