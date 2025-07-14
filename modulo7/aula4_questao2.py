arquivoEntrada = 'frase.txt'
arquivoSaida = 'palavras.txt'

with open(arquivoEntrada, 'r', encoding='utf-8') as leitura:
    conteudo = leitura.read()

palavras = conteudo.split()

palavrasLimpas = []

for palavra in palavras:
    palavraLimpa =''
    for caractere in palavra:
        if caractere.isalpha():
            palavraLimpa += caractere
    
    if palavraLimpa:
        palavrasLimpas.append(palavraLimpa)
    
with open(arquivoSaida, 'w', encoding='utf-8') as escrita:
    for palavra in palavrasLimpas:
        escrita.write(palavra + '\n')
        
with open(arquivoSaida, 'r', encoding='utf-8') as resultado:
    print(resultado.read())