vogais = 'aeiou'
frase = input('Insira uma frase: ')
indices = []
nVogais = 0
for i in range(len(frase)):
    if frase[i] in vogais:
        indices.append(i)
        nVogais += 1
print(f'{nVogais} vogais')
print(f'Índices: {indices}')