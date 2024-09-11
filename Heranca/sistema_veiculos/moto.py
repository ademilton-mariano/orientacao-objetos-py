from veiculo_passeio import VeiculoPasseio

class Moto(VeiculoPasseio):
    def __init__(self, numRodas, combustivel, velocidade, cor, tipo, capacPassageiros, alturaAssento):
        super().__init__(numRodas, combustivel, velocidade, cor, tipo, capacPassageiros)
        self.alturaAssento = alturaAssento

    def __str__(self):
        return f"{super().__str__()}\nAltura do assento: {self.alturaAssento}"