import random


def embaralhar(frase):
    palavras = frase.split()

    palavrasEmbaralhadas = []

    for palavra in palavras:
        if len(palavra) <= 3:
            palavrasEmbaralhadas.append(palavra)
        else:
            primeiraLetra = palavra[0]
            ultimaLetra = palavra[-1]
            miolo = palavra[1:-1]

            listaMiolo = list(miolo)
            random.shuffle(listaMiolo)
            miolhoEmbaralhado = ''.join(listaMiolo)

            palavraNova = primeiraLetra + miolhoEmbaralhado + ultimaLetra
            palavrasEmbaralhadas.append(palavraNova)

    fraseFinal = ' '.join(palavrasEmbaralhadas)
    return fraseFinal


frase = input('Insira uma frase: ')
resultado = embaralhar(frase)
print(f'Frase original: {frase}')
print(f'Frase final: {resultado}')
