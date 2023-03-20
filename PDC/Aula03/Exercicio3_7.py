# Exercício 7-)
# Crie um algoritmo para calcular o salário líquido de um funcionário, considerando
# que seu salário bruto, incide um desconto de 9% em INSS para a previdência.
# O algoritmo deve mostrar o nome do funcionário, o seu salário bruto, o valor de
# desconto de INSS e o seu salário líquido.

# Declaração de variáveis
NameFun = input("Digite o nome do funcionário: ")
SalBrut = float(input("Digite o salário bruto do funcionário: R$"))

# Declaração de variáveis que armazenam valores de resultado
DescINSS = SalBrut * 0.09
SalLiq = SalBrut - DescINSS

# Impressão dos resultados
print("Funcionário:       ", NameFun)
print("Desconto INSS:   R$", DescINSS)
print("Salário Líquido: R$", SalLiq)