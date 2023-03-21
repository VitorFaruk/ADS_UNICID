# Exercício 1-)
# Duas variáveis (A e B) possuem valores distintos (A = 5
# e B = 10, por exemplo). Crie um algoritmo que armazene
# esses valores nas duas variáveis e efetuem a troca de
# valores de forma que a variável A passe a propriedade o
# valor de B e que a variável B passa a propriedade o valor
# de A. Ao final mostrar esses valores trocados.

# Declaração de variáveis
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Troca de valores entre as variáveis
A = B
B = A

# Impressão dos resultados
print("Valor A:", A)
print("Valor B", B)
