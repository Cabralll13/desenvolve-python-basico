frase = input('Digite uma frase: ')
branco = 0
tamanho = len(frase)
for i in range(tamanho):
    if frase[i] == ' ':
        branco += 1

print(f'Espaços em branco: {branco}')