#Lendo as dimensões e o valor da área
comprimento = int(input('Insira o comprimento da área: '))
largura = int(input('Insira a largura da área: '))
valor = float(input('Insira o valor do metro quadrado: '))

#fazendo os cálculos
area = comprimento * largura
preco = valor * area

#Imprimindo os resultados
print(f'O Terreno possui {area}m2 e custa R${preco:,.3f}')