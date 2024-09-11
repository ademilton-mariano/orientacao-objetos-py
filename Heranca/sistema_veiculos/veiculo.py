class Veiculo:
    def __init__(self, numRodas, combustivel, velocidade, cor, tipo):
        self.numRodas = numRodas
        self.combustivel = combustivel
        self.velocidade = velocidade
        self.cor = cor
        self.tipo = tipo
        
    def darPartida(self):
        print(f"{self.tipo} está ligado...")

    def acelerar(self):
        print(f"{self.tipo} está acelerando...")

    def frear(self):
        print(f"{self.tipo} está freando...")

    def __str__(self):
        return f"Número de rodas: {self.numRodas} \nCombustível: {self.combustivel} \nVelocidade: {self.velocidade}\nCor: {self.cor}\nTipo: {self.tipo}"