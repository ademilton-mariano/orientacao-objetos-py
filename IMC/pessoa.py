# criando a classe pessoa 
class Pessoa:
    
    # construtor da classe
    def __init__(self, nome, peso, altura):
        
        # os atributos da classe recebem os valores passados no construtor
        self.nome = nome
        self.peso = peso
        self.altura = altura

    # método para calcular o IMC
    def calcular_imc(self):
        
        # o cálculo do IMC é feito dividindo o peso pela altura ao quadrado
        imc = self.peso / (self.altura ** 2)
        
        # o valor do IMC é retornado
        return imc

    # método para classificar o IMC
    def classificar_imc(self):
        
        # o método calcular_imc da própria classe é chamado para obter o valor do IMC
        imc = self.calcular_imc()
        
        # a classificação do IMC é feita de acordo com os valores estabelecidos
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"