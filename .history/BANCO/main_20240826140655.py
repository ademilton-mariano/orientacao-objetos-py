from conta import ContaBancaria

def main():
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome)

    
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar Saldo")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depositar: "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: "))
        conta.sacar(valor)
    elif opcao == "3":
        saldo = conta.consultar_saldo()
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "4":
        print("Saindo...")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
