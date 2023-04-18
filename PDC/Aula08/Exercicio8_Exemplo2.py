# Exercício Exemplo 2 Aula 08 - Programação de Computadores
# Ler um valor para a variável X, multiplicar esse valor por 3, implicando-o à variável
# de resposta R e apresentar o valor de R obtido, repetindo esta sequência por cinco vezes.
# Somente enquanto o usuário queira.

contador = 1
resposta = "sim"

while (resposta == "sim" or resposta == "s"):
    x = int(input("Digite um valor para x: "))
    r = x * 3
    print("O valor de r é:", r)
    resposta = input("Deseja continuar? ")
    