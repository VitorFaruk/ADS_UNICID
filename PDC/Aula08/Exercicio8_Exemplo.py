# Exercício Exemplo Aula 08 - Programação de Computadores
# Ler um valor para a variável X, multiplicar esse valor por 3, implicando-o à variável
# de resposta R e apresentar o valor de R obtido, repetindo esta sequência por cinco vezes.

contador = 1
while (contador <=5 ):
    x = int(input("Digite um valor para x: "))
    r = x * 3
    print("O valor de R é:", r)
    contador = contador + 1