n1 = int(input('Insira o tamanho da lista 1: '))
lista1 = []
print('Insira os elementos da lista:')
for i in range(n1):
    elemento = int(input())
    lista1.append(elemento)

n2 = int(input('Insira o tamanho da lista 2: '))
lista2 = []
print('Insira os elementos da lista:')
for i in range(n2):
    elemento = int(input())
    lista2.append(elemento)

lista_combinada = []
i = 0
j = 0

while i < len(lista1) and j < len(lista2):
    lista_combinada.append(lista1[i])
    lista_combinada.append(lista2[j])
    i += 1
    j += 1

while i < len(lista1):
    lista_combinada.append(lista1[i])
    i += 1

while j < len(lista2):
    lista_combinada.append(lista2[j])
    j += 1

print("\nA lista combinada de forma alternada é:")
print(lista_combinada)
