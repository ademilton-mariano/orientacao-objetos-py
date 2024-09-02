class Biblioteca:
    
    # Método construtor
    def __init__(self):
        self.livros = []

    # Método para adicionar um livro na lista de livros
    def adicionar_livro(self, livro):
        
        # Adiciona o livro na lista de livros
        self.livros.append(livro)

    # Método para listar os livros da biblioteca
    def listar_livros(self):
        
        # Percorre a lista de livros
        for livro in self.livros:
            
            # Imprime as informações do livro
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")

    # Método para buscar um livro pelo título
    def buscar_livro(self, titulo):
        
        # Percorre a lista de livros
        for livro in self.livros:
            
            # Verifica se o título do livro é igual ao título informado
            if livro.titulo == titulo:
                
                # Retorna o livro encontrado
                return livro
            
        # Caso não encontre o livro, retorna None
        return None
