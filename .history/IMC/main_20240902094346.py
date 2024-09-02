from pessoa import Pessoa

#solicitando os dados do usuário
nome = input("Digite o nome: ")
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

#instanciando a classe Pessoa passando os dados do usuário no construtor
pessoa = Pessoa(nome, peso, altura)

#calculando o IMC do usuário de acordo com os dados informados
imc = pessoa.calcular_imc()

#classificando o IMC do usuário
classificacao = pessoa.classificar_imc()


#imprimindo os dados do usuário
print(f"\nNome: {pessoa.nome}")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")

