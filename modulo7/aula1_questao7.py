import random


def encrypt(listaDeNomes):
    chave = random.randint(1, 10)

    inicioUnicode = 33
    fimUnicode = 126

    tamanhoAlfabeto = fimUnicode - inicioUnicode + 1

    nomesCriptografados = []

    for nome in listaDeNomes:
        nomeCripto = ''
        for caractere in nome:
            valorOriginal = ord(caractere)
            posicaoAlfabeto = valorOriginal - inicioUnicode
            posicaoDeslocada = posicaoAlfabeto + chave
            posicaoFinal = posicaoDeslocada % tamanhoAlfabeto
            valorNovo = posicaoFinal + inicioUnicode
            novoCaractere = chr(valorNovo)
            nomeCripto += novoCaractere

        nomesCriptografados.append(nomeCripto)

    return nomesCriptografados, chave


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomesCifrados, chaveUsada = encrypt(nomes)

print(f"Lista original: {nomes}")
print(f"Chave de criptografia gerada: {chaveUsada}")
print(f"Nomes criptografados: {nomesCifrados}")
