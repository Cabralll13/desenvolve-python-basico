numero = input('Digite seu número de telefone: ')

numeroCorrigido = ''

if len(numero) == 8:
    numeroCorrigido = '9' + numero
elif len(numero) == 9:
    if numero[0] == '9':
        numeroCorrigido = numero
    else:
        print('ERRO: Número de 9 dígitos com formato inválido (não começa com 9).')
else:
    print(f"ERRO: O número {numero} tem um tamanho inválido.")

if numeroCorrigido:
    primeiraParte = numeroCorrigido[:5]
    segundaParte = numeroCorrigido[5:]

    numeroFormatado = primeiraParte + '-' + segundaParte
    print(f'Número completo: {numeroFormatado}')
