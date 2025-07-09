pares = [numero for numero in range(20, 51) if numero % 2 == 0]
quadrado = [numero**2 for numero in range(1, 10)]
divisivelPor7 = [numero for numero in range(1, 101) if numero % 7 == 0]
parImpar = ['par' if n % 2 == 0 else 'ímpar' for n in range(0, 30, 3)]
print(f'Pares entre 20 e 50: {pares}')
print(f'Quadrado dos número de 1 a 9: {quadrado}')
print(f'Divisíveis por 7 de 1 a 100: {divisivelPor7}')
print(f'Pares ou Ímpares: {parImpar}')