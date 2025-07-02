experimentos = int(input('Insira o número de experimentos registrados: '))
i = 0
sapo = 0
rato = 0
coelho = 0
total = 0
while experimentos > i:
    tipo = input(f'Insira o tipo de cobaia usada no experimento {i + 1}(S:Sapo, R:Rato ou C:Coelho): ')
    quantia = int(input('Agora insira a quantidade de cobaias: '))
    if tipo == 'C' or tipo == 'c':
        coelho += quantia
    elif tipo == 'R' or tipo == 'r':
        rato += quantia
    elif tipo == 'S' or tipo == 's':
        sapo += quantia
    
    total += quantia
    i += 1

pCoelhos = coelho / total
pRatos = rato / total
pSapos = sapo / total

print(f'Total: {total} cobaias.')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {pCoelhos}%')
print(f'Percentual de ratos: {pRatos}%')
print(f'Percentual de sapos: {pSapos}%')