import random
lista = [random.randint(-100, 100) for i in range(20)]
mod = sorted(lista)
print('Lista ordenada sem modificar a lista original:')
print(mod)
print('Lista original:')
print(lista)
maior = max(lista)
menor = min(lista)
print('Índice do maior elemento da lista:')
print(lista.index(maior))
print('Índice do menor elemento da lista:')
print(lista.index(menor))