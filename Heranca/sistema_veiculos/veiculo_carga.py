from veiculo import Veiculo

class VeiculoCarga(Veiculo):
    def __init__(self, numRodas, combustivel, velocidade, cor, tipo, capacidadeCarga, numPortas):
        super().__init__(numRodas, combustivel, velocidade, cor, tipo)
        self.capacidadeCarga = capacidadeCarga
        self.numPortas = numPortas
        

    def __str__(self):
        return f"{super().__str__()}\nCapacidade de carga: {self.capacidadeCarga}\nNúmero de portas: {self.numPortas}"
    