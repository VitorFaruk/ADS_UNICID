# Exercício 3 Aula 08 - Programação de Computadores
# Calcular através de um programa que leia a categoria de um
# produto e determine o preço pela tabela: Categoria 1 valor 
# de R$10,00; Categoria 2 valor de R$18,00; Categoria 3 valor
# de R$23,00; Categoria 4 valor de R$26,00 e Categoria 5 valor
# de R$31,00.

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    print("Valor de R$10,00.")
elif categoria == 2:
    print("Valor de R$18,00.")
elif categoria == 3:
    print("Valor de R$23,00.")
elif categoria == 4:
    print("Valor de R$26,00.")
elif categoria == 5:
    print("Valor de R$31,00.")
else:
    print("A categoria digitada não é válida.")