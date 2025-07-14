mesesDoAno = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

partesData = data.split('/')

dia, mes, ano = partesData
dia, mes, ano = int(dia), int(mes), int(ano)

nomeMes = mesesDoAno[mes - 1]
print(f'Você nasceu em {dia} de {nomeMes} de {ano}.')