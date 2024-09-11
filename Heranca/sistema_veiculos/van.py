from veiculo_carga import VeiculoCarga

class Van(VeiculoCarga):
    def __init__(self, numRodas, combustivel, velocidade, cor, tipo, capacidadeCarga, numPortas, qtd_caixas):
        super().__init__(numRodas, combustivel, velocidade, cor, tipo, capacidadeCarga, numPortas)
        self.qtd_caixas = qtd_caixas
        
    def __str__(self):
        return f"{super().__str__()}\nQuantidade de caixas: {self.qtd_caixas}"
        
    def carregarVan(self):
        print("Van está sendo carregada...")  