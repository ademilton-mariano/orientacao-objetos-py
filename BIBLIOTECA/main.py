from livro import Livro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            titulo = input("Digite o título do livro a buscar: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")
            else:
                print("Livro não encontrado.")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
