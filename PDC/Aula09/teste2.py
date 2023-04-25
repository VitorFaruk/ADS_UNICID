# Aula 09 (Programação de computadores) - Lista

lista_simples=[1,2,3,4,5,6,7,8,9]
lista_3por3=[[1,2,3],[4,5,6],[7,8,9]]
lista_tuple=((1,2,3),(4,5,6),(7,8,9))
tamanho_lista_simples=len(lista_simples)
tamanho_lista_3por3 = len(lista_3por3)

print(lista_simples)
print(lista_3por3)
print(lista_tuple)
print("Quantidade de posição lista simples: ", tamanho_lista_simples)
print("Quantidade de posições lista 3 por 3: ", tamanho_lista_3por3)

quartoelemento_listasimples = lista_simples[3]
# Linha ( [1] ) e coluna ( [2] ), então, o elemento a ser exibido é 6.
terceiroelem_segundalinha_lista3por3 = lista_3por3[1][2]

print("Quarto elemento da lista simples: ", quartoelemento_listasimples)
print("Terceiro elemento da segunda linha lista 3 por 3: ", terceiroelem_segundalinha_lista3por3)

lista_simples[3] = 100
lista_3por3[1][2] = 200

print(lista_simples)
print(lista_3por3)