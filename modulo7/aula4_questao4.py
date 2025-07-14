import random

arquivoPalavras = 'gabarito_forca.txt'
arquivoForcaArt = 'gabarito_enforcado.txt'

def carregarPalavraAleatoria():
    with open(arquivoPalavras, 'r', encoding='utf-8') as f:
        palavras = f.read().splitlines()
    return random.choice(palavras).lower()

def carregarEstagiosForca():
    with open(arquivoForcaArt, 'r', encoding='utf-8') as f:
        estagios = f.read().strip().split('=========')
    return [estagio.strip() for estagio in estagios]

def imprimeEnforcado(erros, estagios):
    if 0 <= erros < len(estagios):
        print(estagios[erros])

def jogar():
    palavraSecreta = carregarPalavraAleatoria()
    estagiosForca = carregarEstagiosForca()

    letrasCorretas = []
    letrasErradas = []
    erros = 0
    maxTentativas = 6
    print("="*40)
    print("   Bem-vindo ao Jogo da Forca!")
    print("="*40)

    while erros < maxTentativas:
        palavraMostrada = ''
        for letra in palavraSecreta:
            if letra in letrasCorretas:
                palavraMostrada += letra + ' '
            else:
                palavraMostrada += '_ '

        print("\nPalavra: ", palavraMostrada)
        print(f"Letras erradas: {' '.join(letrasErradas)}")

        if '_' not in palavraMostrada:
            print('\nParabéns! Você adivinhou a palavra!')
            break

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in letrasCorretas or tentativa in letrasErradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if tentativa in palavraSecreta:
            print("Bom palpite!")
            letrasCorretas.append(tentativa)
        else:
            print("Letra incorreta!")
            erros += 1
            letrasErradas.append(tentativa)
            imprimeEnforcado(erros, estagiosForca)

    if erros == maxTentativas:
        print("\n" + "="*40)
        print("Fim de jogo! Você foi enforcado.")
        print(f"A palavra secreta era: '{palavraSecreta}'")
        print("="*40)

jogar()