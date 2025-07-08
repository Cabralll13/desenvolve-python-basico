import random

lista1, lista2 = [],[]
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))
    
print(f'Lista 1 - {lista1}')
print(f'Lista 2 - {lista2}')

interseccao = []
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento)
interseccao.sort()

print(f'Instersecção - {interseccao}')

print('Contagem')
for i in interseccao:
    print(f'{i}: (lista 1={lista1.count(i)}, lista 2={lista2.count(i)})')