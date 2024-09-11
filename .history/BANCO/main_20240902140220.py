from conta import ContaBancaria

# Função principal
def main():
    
    # Solicita o nome do titular da conta
    nome = input("Digite o nome do titular da conta: ")
    
    # Instancia a classe ContaBancaria passando o nome do titular como argumento
    conta = ContaBancaria(nome)

    
    
    # Loop principal
    while True:
        # Menu
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar Saldo")
        print("4. Sair")
        
        # Opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        # Verifica a opção escolhida
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
            break
        else:
            print("Opção inválida.")
            break

# Chamada da função principal, que inicia o programa caso este arquivo seja executado
if __name__ == "__main__":
    main()
