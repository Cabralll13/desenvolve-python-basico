frase = input('Digite uma frase: ')
vogais = 'aeiouAEIOU'
consoantes = 'qwrtypsdfghjklzxcvbnmçQWRTYPSDFGHJKLÇZXCVBNM'
vogalEncontrada = [letra for letra in frase if letra in vogais]
consoanteEncontrada = [letra for letra in frase if letra in consoantes]

print(f'Vogais: {vogalEncontrada}')
print(f'Consoantes: {consoanteEncontrada}')