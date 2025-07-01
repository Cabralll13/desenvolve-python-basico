avaliacao = int(input("Digite a avaliação do filme (1 a 5): "))
if avaliacao == 5:
    print("Excelente filme!")
elif avaliacao == 4:
    print("Muito bom!")
elif avaliacao == 3:
    print("Bom.")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim!")
else:
    print("Avaliação inválida. Digite um número de 1 a 5.")