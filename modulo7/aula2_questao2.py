vogais = 'aeiouAEIOU'
frase = input('Digite uma frase: ')

for vogal in vogais:
    frase = frase.replace(vogal, '*')
print(f'Frase modificada: {frase}')