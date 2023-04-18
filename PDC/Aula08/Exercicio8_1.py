# Exercício 1 Aula 08 - Programação de Computadores
# Programa que solicita a idade do carro do usuário e, em seguida, escreve "novo"
# se o carro tiver menos de três anos; ou "velho", caso contrário

idade = int(input("Digite a idade do carro: "))

if idade < 3:
    print("Novo.")
else:
    print("Velho.")
