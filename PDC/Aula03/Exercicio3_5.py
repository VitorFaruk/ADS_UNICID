# Exercício 5-)
# Uma empresa de vendas de softwares paga a seu vendedor um fixo de
# R$ 800,00 por mês, mais uma comissão de 15% pelo seu valor de 
# vendas no mês. Faça um algoritmo que leia o valor da venda e
# determine o salário total do funcionário.

# Declaração de variável
ValVd = float (input("Digite o valor total de vendas: R$"))

# Declaração de variáveis que armazenam valores de resultado
ComisVd = ValVd * 0.15
SalFix = 800.00
SalTot = ValVd + 800

# Impressão dos resultados
print("Salário Fixo: R$", SalFix)
print("Comissão Ven: R$", ComisVd)
print("Total Salar.: R$", SalTot)