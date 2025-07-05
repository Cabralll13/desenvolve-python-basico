from datetime import datetime
data_atual = datetime.now()
data = data_atual.strftime('%d/%m/%Y')
hora = data_atual.strftime('%H:%M')
print(f'Data: {data}')
print(f'Hora: {hora}')
