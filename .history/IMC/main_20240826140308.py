from pessoa import Pessoa


nome = input("Digite o nome: ")
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

pessoa = Pessoa(nome, peso, altura)

imc = pessoa.calcular_imc()
classificacao = pessoa.classificar_imc()

print(f"\nNome: {pessoa.nome}")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")

