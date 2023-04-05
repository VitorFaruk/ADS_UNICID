# Definição e armazenamento de valores nas variáveis
print("--------Cadastro de funcionário--------")
nome = input("Digite o seu nome: ")
salariobruto = float(input("Digite o seu salário: R$"))
desconto = salariobruto*(9/100)
salarioliquido = salariobruto - desconto
print("---------------------------------------")

# Separando os blocos por uma linha
print("")

# Exibição de valores
print("----------Dados do funcionário---------")
print("Nome do funcionário: ", nome)
print("Salário bruto: R$", salariobruto)
print("Desconto: R$", desconto)
print("Salário líquido: R$", salarioliquido)
print("---------------------------------------")
