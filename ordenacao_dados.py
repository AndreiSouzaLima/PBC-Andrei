#Escreva um programa Python que implemente um algoritmo de ordenação de dados, como o quicksort ou mergesort.
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x < pivo]
        maiores = [x for x in lista[1:] if x >= pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

lista = [5, 2, 8, 3, 1, 9]
lista_ordenada = quicksort(lista)
print(lista_ordenada)