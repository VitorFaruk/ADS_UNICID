# Exercício Teste Aula 08 - Programação de Computadores

import math
print("--------OPERAÇÃO -> NÚMERO---------")
print("Raiz quadrada               -> 1")
print("Potenciação                 -> 2")
print("Cosseno em radiano          -> 3")
print("Seno em radiano             -> 4")
print("Tangente em radiano         -> 5")
print("Converter graus em radianos -> 6")
print("Número PI                   -> 7")
print("Hipotenusa de dois números  -> 8")
print("-----------------------------------")

tipo = int(input("\nDigite o número da operação que você deseja? "))

if tipo == 1:
    num = int(input("Digite um valor para observar a raiz quadrada: "))
    print("A raiz quadrada é:", math.sqrt(num))
elif tipo == 2:
    num = int(input("Digite o valor da base: "))
    numdois = int(input("Digite o valor da potência: "))
    print("O valor dessa potenciação é:", math.pow(num, numdois))
elif tipo == 3:
    num = int(input("Digite um número para observar seu cosseno em radiano: "))
    print("O valor do cosseno em radiano é:", math.cos(num))
elif tipo == 4:
    num = int(input("Digite um número para observar seu seno em radiano: "))
    print("O valor do seno em radiano é:", math.sin(num))
elif tipo == 5:
    num = int(input("Digite um número para observar sua tangente em radiano: "))
    print("O valor da tangente em radiano é:", math.tan(num))
elif tipo == 6:
    num = float(input("Digite um valor de graus para observar em radiano: "))
    print("O valor de graus em radiano é", math.radians(num))
elif tipo == 7:
    print("O valor de PI é:", math.pi)
elif tipo == 8:
    num = int(input("Digite o número do primeiro cateto: "))
    numdois = int(input("Digite o número do segunda cateto: "))
    print("A hipotenusa dos números fornecidos é:", math.hypot(num, numdois))
else:
    print("Categoria inválida.") 