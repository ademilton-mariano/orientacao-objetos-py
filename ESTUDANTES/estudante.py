class Estudante:
    
    # Construtor
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    # Método para exibir informações do estudante
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"

    # Método para alterar o curso do estudante
    def alterar_curso(self, novo_curso):
        
        # Altera o curso do estudante
        self.curso = novo_curso
        print(f"Curso alterado para {novo_curso}.")
