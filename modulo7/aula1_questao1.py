nome = input('Digite seu nome: ')
tamanho = len(nome)
temp = ""
for i in range(tamanho):
    temp += nome[i]
    print(temp)
