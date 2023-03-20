# Exercício 6-)
# Uma empresa de desenvolvimento de software paga ao seu vendedor um salário
# fixo de R$ 500,00 por mês, mais um bônus de R$50,00 por sistema vendido.
# Faça um algoritmo que leia quantos softwares o funcionário vendeu e
# determine o salário total do funcionário.

# Declaração de variável
QtdSof = float(input("Digite a quantidade de Softwares vendidos: "))

# Declaração de variáveis que armazenam valores de resultado
TotBon = QtdSof * 50.00
SalFix = 500.00
TotSal = TotBon + SalFix

# Impressão dos resultados
print("Valor total de bônus: R$", TotBon)
print("Valor total Sal. F..: R$", SalFix)
print("Valor total do Salá.: R$", TotSal)