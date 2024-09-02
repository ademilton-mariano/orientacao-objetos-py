from produto import Produto
from pedido import Pedido

def main():
    pedido = Pedido()

    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Calcular Total")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            produto = Produto(nome, preco)
            pedido.adicionar_produto(produto)
        elif opcao == "2":
            total = pedido.calcular_total()
            print(f"Valor total do pedido: R$ {total:.2f}")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
