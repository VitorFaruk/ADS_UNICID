# Exercício 3-)
# O sistema de avaliação de determinada disciplina é composto por
# três provas. A primeira prova tem peso 2, a segunda prova tem
# peso 3, e a terceira prova tem peso 5. Faça um algoritmo
# para calcular a média final de um aluno nesta disciplina.

# Declaração de variáveis
NoteF = float(input("Digite a primeira nota:"))
NoteS = float(input("Digite a segunda nota:"))
NoteT = float(input("Digite a terceira nota:"))

# Impressão das notas digitadas
print("Primeira nota:", NoteF)
print("Segunda nota: ", NoteS)
print("Terceira nota:", NoteT)

# Atribuição das notas conforme o peso da disciplina
NoteF = NoteF * 0.2
NoteS = NoteS * 0.3
NoteT = NoteT * 0.5

# Declaração de variável que armazena valor de resultado
NoteMedium = NoteF + NoteS + NoteT

# Impressão do resultado
print("A Média do aluno é: ", NoteMedium)