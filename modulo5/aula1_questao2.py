import random
import math
n = int(input('Insira a quantidade de números aleatórios que deseja criar: '))
soma = 0
for i in range(n):
    soma += random.randint(0, 100)
soma = math.sqrt(soma)
print(f'Resultado: {soma}.')
