frase = input('Digite uma frase: ')
objetivo = sorted(input('Digite a palavra objetivo: '))
anagrama = []
listaPalavras = frase.lower().split()
for palavra in listaPalavras:
    if sorted(palavra) == objetivo:
        anagrama.append(palavra)
print(f'Anagramas: {anagrama}')