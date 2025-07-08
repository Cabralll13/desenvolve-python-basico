import random
numElementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for i in range(numElementos)]
print('Lista:')
print(elementos)
print('Soma dos elementos da lista:')
print(sum(elementos))
print('Média dos elementos da lista:')
print(sum(elementos)/len(elementos))