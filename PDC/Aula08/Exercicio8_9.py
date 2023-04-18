# Exercício 9 Aula 08 - Programação de Computadores
# Desenvolva um programa que leia duas notas e calcule a média
# aritmética. O programa deverá efetuar o cálculo da média para
# 5 alunos, armazenando também os seus nomes, e imprimir na tela
# qual aluno obteve a maior média e qual foi o valor desta média.

contador = 0
mediam = 0
nomem = ""
while (contador < 5):
    contador += 1
    nomev = input("Escreva o nome do aluno: ")
    notaum = float(input("Digite a primeira nota: "))
    notadois = float(input("Digite a segunda nota: "))
    mediav = (notaum + notadois) / 2
    print("A média do aluno é:", str(mediav) + "\n")
    
    if (mediav > mediam):
        mediam = mediav
        nomem = nomev
        
print("O aluno com maior média é:")
print("Aluno:", nomem) 
print("Média:", mediam)