import random
n = random.randint(1, 10)
m = 0
while m != n:
    m = int(input('Adivinhe o número entre 1 e 10: '))
    if (m - n) > 0:
        print('Tente um número menor.')
    elif (m - n) < 0:
        print('Tente um número maior.')
print(f'Correto! O número é {n}.')