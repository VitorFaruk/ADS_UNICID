# Exercício 2-)
# O custo ao consumidor de um carro novo, é a soma do custo de
# fábrica com a porcentagem do revendedor e com o custo dos
# impostos (aplicados ao custo da fábrica). Suponde que a
# porcentagem do revendedor seja de 25% do custo de fábrica
# e que os impostos custam 45% do custo de fábrica, faça
# um algoritmo que leia o valor de custo de fábrica e
# determine o preço do automóvel para o consumidor.

# Declaração de variável
CustoDeFabrica = int(input ("Digite o valor do Custo de Fábrica:"))

# Declaração de variáveis que armazenam valores de resultado
CustoRevendedor = (CustoDeFabrica/100) * 25
CustoImpostos = (CustoDeFabrica/100) * 45
CustoConsumidor = CustoRevendedor + CustoImpostos

# Impressão dos resultados
print("Custo de Fábrica: R$", CustoDeFabrica)
print("Custo Revendedor: R$", CustoRevendedor)
print("Custo de Impostos: R$", CustoImpostos)
print("Custo do Consumidor: R$", CustoConsumidor)