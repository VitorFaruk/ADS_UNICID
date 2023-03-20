# Exercício 9-)
# Analisando a fórmula: Prestação = valor + (valor * (taxa/100) * tempo)
# Crie um algoritmo para efetuar o cálculo do valor de uma prestação em atraso.

# Declaração de varíaveis
Pres = int(input("Digite o valor da prestação (R$):"))
Taxa = float(input("Digite a taxa de juros (%):"))
Temp = int(input("Digite o número de dias em atraso: "))

# Declaração de variável que armazena valor de resultado
PresAtr = Pres + (Pres * (Taxa/100) * Temp)

# Impressão do resultado
print("O valor da prestação em atraso é: R$", PresAtr)