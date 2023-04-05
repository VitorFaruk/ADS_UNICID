# Uma revendedora de automóveis paga a seu vendedor um fixo de R$ 2000,00 por mês, 
# mais uma comissão de 2% sobre o valor total vendido (em reais) no mês. Considerando 
# que sobre o salário bruto (salário fixo mais comissão) incide um desconto de 9% em INSS 
# para a previdência, faça um algoritmo que leia o valor das vendas do mês e calcule o 
# valor dos salários bruto e líquido de um vendedor, exibindo estes dois valores na tela.

# Definição de variáveis

salariofixo = 2000
valordasvendas = float(input('Digite o valor das vendas: R$'))
comissao = valordasvendas * (2/100) 
salariobruto = salariofixo + comissao
salarioliquido = salariobruto - (salariobruto*0.09)

# Exibição dos valores
print('Valor do salário bruto: R$', salariobruto)
print('Valor do salário líquido: R$', salarioliquido)