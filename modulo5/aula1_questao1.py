n1 = float(input('Insira um número decimal: '))
n2 = float(input('Insira outro número decimal: '))
resultado = n1 - n2
resultado = abs(resultado)
resultado = round(resultado, 2)
print(f'A diferença absoluta entre os número é: {resultado}')
