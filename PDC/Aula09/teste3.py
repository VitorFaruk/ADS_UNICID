# Aula 09 (Programação de computadores) - Operações matemáticas com lista

import numpy as np
lista_array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
lista_array2 = 2 * lista_array1
primeiralinha_array1 = lista_array1[0, :]
primeiracoluna_array1 = lista_array1[1:, 0]
print(lista_array2)

print("Primeira linha array 1: ", primeiralinha_array1)
print("Todos os primeiros elementos a partir da segunda linha do array: ",primeiracoluna_array1)

array_multiplicacao = lista_array1*lista_array2
print("Multiplicação do array 1 com array 2:\n", array_multiplicacao)

array_divisao = lista_array1/lista_array2
print("Divisão do array 1 pelo array 2:\n", array_divisao)

array_soma = lista_array1+lista_array2
print("Soma de array 1 com array 2:\n", array_soma)

array_subtracao = lista_array1 - lista_array2
print("Subtração de array 1 pelo array 2:\n", array_subtracao)

#Transformando linha em coluna
array_transposicao = lista_array1.transpose()
print("Transpondo linhas em colunas do array 1:\n", array_transposicao)