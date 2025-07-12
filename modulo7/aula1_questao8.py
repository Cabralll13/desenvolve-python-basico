def validaCpf(cpfFornecido):
    numeros = ""
    for char in cpfFornecido:
        if char in "0123456789":
            numeros += char

    if len(numeros) != 11 or len(set(numeros)) == 1:
        return False

    cpfBase = numeros[:9]
    digitosFornecidos = numeros[9:]

    somaD1 = 0
    multiplicador = 10
    for digito in cpfBase:
        somaD1 += int(digito) * multiplicador
        multiplicador -= 1

    resto = somaD1 % 11
    d1Calculado = 0 if resto < 2 else 11 - resto

    cpfBaseComD1 = cpfBase + str(d1Calculado)

    somaD2 = 0
    multiplicador = 11
    for digito in cpfBaseComD1:
        somaD2 += int(digito) * multiplicador
        multiplicador -= 1

    resto = somaD2 % 11
    d2Calculado = 0 if resto < 2 else 11 - resto

    digitosCalculados = f"{d1Calculado}{d2Calculado}"

    return digitosCalculados == digitosFornecidos


cpfUsuario = input("Digite um CPF no forma XXX.XXX.XXX-XX: ")

if validaCpf(cpfUsuario):
    print("Válido")
else:
    print("Inválido")
