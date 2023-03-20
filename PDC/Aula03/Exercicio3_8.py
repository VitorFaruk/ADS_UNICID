# Exercício 8-)
# Considerando que para um consórcio, sabe-se o número total de prestações,
# a quantidade de prestações pagas e o valor atual da prestação, escreva
# um algoritmo que determine o total pago pelo consorciado e o saldo devedor.

# Declaração de variáveis
NumPres = int(input("Digite o número de prestações do consórcio:"))
NumPresP = int(input("Digite o número de prestações pagas:"))
ValPres = float(input("Digite o valor atual da prestação: "))

# Declaração de variáveis que armazenam valores de resultado
TotPag = NumPresP * ValPres
SalDev = (NumPres * ValPres) - TotPag

# Impressão dos resultados
print("Valor total pago: R$", TotPag)
print("Saldo devedor   : R$", SalDev)