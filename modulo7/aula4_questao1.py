import os
frase = input('Digite uma frase: ')
nomeArquivo = 'frase.txt'

with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(frase)
    
caminho = os.path.abspath(nomeArquivo)
print(f'Frase salva em {caminho}')