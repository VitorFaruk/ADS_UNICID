# Exercício 2 Aula 08 - Programação de Computadores
# Programa para calcular a conta de um telefone celular. Os planos
# da empresa apresentam planos diferentes de acordo com a quantia
# de minutos usados por mês. Abaixo de 200 minutos, a empresa cobra
# R$0,20 por minuto. Entre 200 a 400 minutos, o preço é de R$0,18.
# Acima de 400 minutos, o preço por minuto é de R$0,15.

minutos = int(input("Digite quantos minutos você utilizou nesse mês: "))

if minutos < 200:
    valor = minutos * 0.20
    print("O valor da conta mensal é: R$", valor)
elif minutos > 200 and minutos < 400:
    valor = minutos * 0.18
    print("O valor da conta mensal é: R$", valor)
else:
    valor = minutos * 0.15
    print("O valor da conta mensal é: R$", valor)
