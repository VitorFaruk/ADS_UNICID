# Exercício 4-)
# Um cliente de um banco tem um saldo positivo de R$ 500,00. Faça
# um algoritmo que leia um cheque que entrou e calcule o saldo.

# Declaração de variáveis
SaldoCliente = 500.00
Cheque = float(input("Digite o valor do cheque: "))

# Declaração de variável que armazena valor de resultado
TotalSaldo = SaldoCliente - Cheque

# Impressão dos resultados
print("Debitado R$", Cheque, " de R$", SaldoCliente)
print("Saldo atual do Cliente: R$", TotalSaldo)