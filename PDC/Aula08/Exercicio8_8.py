# Exercício 8 Aula 08 - Programação de Computadores
# Crie um algoritmo que imprima na tela os 10 primeiros números
# ímpares de 1 a 50 que sejam divisíveis por 5 e 7.

contador = 0
num = 0
while (contador < 10):
    num += 1
    if num%2 == 1 and (num%5 == 0 and num%7 == 0):
        print(num)
        contador += 1