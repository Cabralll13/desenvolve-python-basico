nomeArquivo = 'estomago.txt'

with open(nomeArquivo, 'r', encoding='latin-1') as arquivo:
    linhas = arquivo.readlines()

print("--- As primeiras 25 linhas do roteiro ---")
for linha in linhas[:25]:
    print(linha.strip())

totalLinhas = len(linhas)
print("\n" + "-"*50)
print(f"Número total de linhas no arquivo: {totalLinhas}")
print("-" * 50)

maiorLinha = ''
for linha in linhas:
    if len(linha) > len(maiorLinha):
        maiorLinha = linha

print("\n--- Linha com maior número de caracteres ---")
print(f"Comprimento: {len(maiorLinha.strip())} caracteres")
print(f"Conteúdo: {maiorLinha.strip()}")
print("-" * 50)

conteudo = "".join(linhas)
    
textoLower = conteudo.lower()
pontuacao = '.,!?;:"()[]'
texto = textoLower

for p in pontuacao:
    texto = texto.replace(p, ' ')
    
listaPalavras = texto.split()

contagemNonato = listaPalavras.count('nonato')
contagemIria = listaPalavras.count('íria')

print("\n--- Menções aos Personagens ---")
print(f"O nome 'Nonato' foi mencionado {contagemNonato} vez(es).")
print(f"O nome 'Íria' foi mencionado {contagemIria} vez(es).")
print("="*50)