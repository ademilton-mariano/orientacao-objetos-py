from estudante import Estudante
from gerenciador import GerenciadorEstudantes

def main():
    # Cria um gerenciador de estudantes
    gerenciador = GerenciadorEstudantes()

    while True:
        print("\nMenu:")
        print("1. Adicionar Estudante")
        print("2. Listar Estudantes")
        print("3. Buscar Estudante")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do estudante: ")
            idade = int(input("Digite a idade do estudante: "))
            curso = input("Digite o curso do estudante: ")
            estudante = Estudante(nome, idade, curso)
            gerenciador.adicionar_estudante(estudante)
        elif opcao == "2":
            gerenciador.listar_estudantes()
        elif opcao == "3":
            nome = input("Digite o nome do estudante a ser buscado: ")
            estudante = gerenciador.buscar_estudante(nome)
            if estudante:
                print(estudante.exibir_informacoes())
            else:
                print("Estudante não encontrado.")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
