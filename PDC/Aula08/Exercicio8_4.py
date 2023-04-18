# Exercício 4 Aula 08 - Programação de Computadores
# Programa que calcula a média aritmética da nota de duas
# provas e decide se o aluno passou (média maior que 6), 
# se está de recuperação (média menor que 6 e maior que 1),
# se reprovou direto (média menor que 1), ou se teve
# aproveitamento excelente (média maior do que 9).

provaum = float(input("Digite a nota da primeira prova: "))
provadois = float(input("Digite a nota da segunda prova: "))

media = (provaum + provadois) / 2

if media >= 9:
    print("Aluno aprovado. Aproveitamento excelente!")
elif media < 9 and media > 6:
    print("Aluno aprovado.")
elif media < 6 and media >= 1:
    print("Aluno de recuperação.")
else:
    print("Aluno reprovado.")