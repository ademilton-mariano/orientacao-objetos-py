class GerenciadorEstudantes:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)
        print(f"Estudante {estudante.nome} adicionado com sucesso.")

    def listar_estudantes(self):
        if not self.estudantes:
            print("Nenhum estudante cadastrado.")
        else:
            for estudante in self.estudantes:
                print(estudante.exibir_informacoes())

    def buscar_estudante(self, nome):
        for estudante in self.estudantes:
            if estudante.nome == nome:
                return estudante
        return None
