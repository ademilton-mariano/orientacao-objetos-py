from veiculo_carga import VeiculoCarga

class Caminhao(VeiculoCarga):
    def __init__(self, numRodas, combustivel, velocidade, cor, tipo, capacidadeCarga, numPortas, tam_container):
        super().__init__(numRodas, combustivel, velocidade, cor, tipo, capacidadeCarga, numPortas)
        self.tam_container = tam_container
    
    def __str__(self):
        return f"{super().__str__()}\nTamanho do container: {self.tam_container}"
        
    def carregarCaminhao(self):
        print("Caminhão está sendo carregado...")