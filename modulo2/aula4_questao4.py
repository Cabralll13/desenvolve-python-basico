valor = int(input('Insira o valor da quantia em reais: '))

n100 = valor // 100
valor = valor % 100
n50 = valor // 50
valor = valor % 50
n20 = valor // 20
valor = valor % 20
n10 = valor // 10
valor = valor % 10
n5 = valor // 5
valor = valor % 5
n2 = valor // 2
valor = valor % 2
n1 = valor


print(f'{n100} notas de 100')
print(f'{n50} notas de 50')
print(f'{n20} notas de 20')
print(f'{n10} notas de 10')
print(f'{n5} notas de 5')
print(f'{n2} notas de 2')
print(f'{n1} notas de 1')