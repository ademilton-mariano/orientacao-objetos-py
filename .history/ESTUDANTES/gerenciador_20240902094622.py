class GerenciadorEstudantes:
    
    # Inicializa a lista de estudantes
    def __init__(self):
        self.estudantes = []

    # Adiciona um estudante na lista de estudantes
    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)
        print(f"Estudante {estudante.nome} adicionado com sucesso.")

    # Lista os estudantes cadastrados
    def listar_estudantes(self):
        
        # Verifica se a lista de estudantes está vazia
        if not self.estudantes:
            print("Nenhum estudante cadastrado.")
            
        # Caso contrário, percorre a lista de estudantes
        else:
            for estudante in self.estudantes:
                print(estudante.exibir_informacoes())

    def buscar_estudante(self, nome):
        for estudante in self.estudantes:
            if estudante.nome == nome:
                return estudante
        return None
