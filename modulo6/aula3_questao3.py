import random
lista = []
for i in range(20):
    lista.append(random.randint(-10, 10))

print(f'Lista: {lista}')
melhorPosicao = -1
maiorTamanho = 0

posicaoAtual = -1
tamanhoAtual = 0

for i in range(len(lista)):
    numero = lista[i]

    if numero < 0:
        tamanhoAtual += 1
        if posicaoAtual == -1:
            posicaoAtual = i
    else:
        if tamanhoAtual > maiorTamanho:
            maiorTamanho = tamanhoAtual
            melhorPosicao = posicaoAtual
        tamanhoAtual = 0
        posicaoAtual = -1

if tamanhoAtual > maiorTamanho:
    maiorTamanho = tamanhoAtual
    melhorPosicao = posicaoAtual

if melhorPosicao != -1:
    del lista[melhorPosicao: melhorPosicao + maiorTamanho]
print(f'Lista editada: {lista}')
