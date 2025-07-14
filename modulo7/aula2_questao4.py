def validadorSenha(senha):
    if len(senha) < 8:
        return False
    maiuscula = False
    minuscula = False
    numero = False
    especial = False

    for char in senha:
        if 'a' <= char <= 'z':
            minuscula = True
        elif 'A' <= char <= 'Z':
            maiuscula = True
        elif '0' <= char <= '9':
            numero = True
        else:
            especial = True
    if maiuscula and minuscula and numero and especial:
        return True
    else:
        return False


senha = input('Insira a senha: ')
if validadorSenha(senha):
    print(True)
else:
    print(False)
