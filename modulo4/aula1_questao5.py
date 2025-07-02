n = int(input('Insira a quantidade de respondentes: '))
i = 1
media = 0
while n > i:
    idade = int(input(f'Insira a idade da pessoa {i}: '))
    media += idade
    i += 1

media /= n
print(f'Média das idades: {media}.')