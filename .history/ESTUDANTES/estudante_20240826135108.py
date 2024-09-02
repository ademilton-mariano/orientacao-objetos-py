class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        print(f"Curso alterado para {novo_curso}.")
