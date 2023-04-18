# Exercício Exemplo 3 Aula 08 - Programação de Computadores
# Calcule o fatorial de um número digitado.

fatorial = contador = 1
num = int(input("Digite um número: "))
while (contador <= num):
    fatorial = fatorial * contador
    contador += 1
print("O fatorial de",num,"é:", fatorial)