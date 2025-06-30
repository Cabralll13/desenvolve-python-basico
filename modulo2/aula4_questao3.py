p1 = input('Nome do produto 1: ')
valor1 = float(input('Valor unitário do produto 1: '))
quan1 = int(input('Quantida comprada do produto 1: '))

p2 = input('Nome do produto 2: ')
valor2 = float(input('Valor unitário do produto 2: '))
quan2 = int(input('Quantida comprada do produto 2: '))

p3 = input('Nome do produto 3: ')
valor3 = float(input('Valor unitário do produto 3: '))
quan3 = int(input('Quantida comprada do produto 3: '))

total = (valor1 * quan1) + (valor2 * quan2) + (valor3 * quan3)

print(f'Total: {total:,.2f}')