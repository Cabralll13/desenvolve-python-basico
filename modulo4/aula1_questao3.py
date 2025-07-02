n1 = int(input('Insira o valor de n1: '))
n2 = int(input('Insira o valor de n2: '))
n3 = int(input('Insira o valor de n3: '))
m = (n1 + n2 + n3) / 3
if m>=60:
    print('Aprovado.')
elif m>=40:
    print('Recuperação')
else:
    print('Reprovado')
print('Fim.')