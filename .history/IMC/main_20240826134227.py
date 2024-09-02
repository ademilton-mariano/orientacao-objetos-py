from pessoa import Pessoa

def main():
    nome = input("Digite o nome: ")
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    pessoa = Pessoa(nome, peso, altura)

    imc = pessoa.calcular_imc()
    classificacao = pessoa.classificar_imc()

    print(f"\nNome: {pessoa.nome}")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()
