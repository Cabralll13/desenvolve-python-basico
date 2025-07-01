idade = int(input('Insira sua idade: '))
genero = input('Insira seu gênero (M ou F): ')
tempo = int(input('Insira seu tempo de serviço em anos: '))
aposentar = (genero == 'F' and (idade > 60 or tempo >= 30 or (idade > 60 and tempo >=25))) or (genero == 'F' and (idade > 65 or tempo >= 30 or (idade > 60 and tempo >=25)) )