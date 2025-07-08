lista = []
print('Insira os elementos da lista (insira 0 para terminar):')
n = 1
while n != 0:
    n = int(input())
    if n != 0:
        lista.append(n)
print(f'Lista: {lista}')
print(f'3 primeiros elementos da lista: {lista[0:3]}')
print(f'Os 2 último elementos: {lista[-2:]}')
print(f'Lista invertida: {lista[::-1]}')
print(f'Elementos de índice par: {lista[0:: 2]}')
print(f'Elementos com índices ímpares: {lista[1::2]}')
