# Exercício 4.3-) Crie um algoritmo que imprima na tela os
# 20 primeiros números divisíveis por três que sejam maiores
# do que 16.

# Definição de variáveis
contador = 1
numero = 0
posicao = 0

# Abertura laço de repetição até 20 números
while (contador <= 20):
    # Somatória dos valores do número
    numero = numero + 1
    # Abertura condição se maior que 16 e divisível por 3
    if (numero > 16) and (numero % 3 == 0):
        # Somatória das posições
        posicao = posicao + 1
        # Impressão da posição e o número referente
        print("O número de posição", posicao,"é:", numero)
        # Contador de até 20 primeiros números
        contador = contador + 1