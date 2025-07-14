def palindromo(frase):
    fraseLimpa = ''
    for char in frase.lower():
        if ('a' <= char <= 'z') or ('0' <= char <= '9'):
            fraseLimpa += char
    fraseReversa = fraseLimpa[::-1]
    return fraseLimpa == fraseReversa


while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        print("Programa encerrado.")
        break

    if palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
