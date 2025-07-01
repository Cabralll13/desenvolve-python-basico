distancia = float(input("Digite a distância em km: "))
peso = float(input("Digite o peso em kg: "))
if distancia <= 100:
    valor = peso
elif distancia > 100 and distancia < 300:
    valor = peso * 1.5
else:
    valor = peso * 2.0
if peso > 10:
    valor += 10
print(f"O valor do frete é: R$ {valor:.2f}")
