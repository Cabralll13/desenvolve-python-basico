horasTrabalhadas = [40, 37, 45, 40, 40, 48]
ganhoPorHora = 20
horaExtra = 25
pagamentos = [ganhoPorHora * min(hora, 40) + horaExtra * max(0, hora-40)
              for hora in horasTrabalhadas]
print(pagamentos)
