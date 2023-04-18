# Exercício 6 Aula 08 - Programação de Computadores
# Crie um algoritmo que imprima na tela os 20 primeiros números
# divisíveis por 3 que sejam maiores do que 50.

contador = 0
num = 0

while (contador < 20):
    num += 1
    if num > 50 and num%3 == 0:
        print(num)
        contador += 1