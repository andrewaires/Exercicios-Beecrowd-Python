while True:
    try:
        numero = input()
        divisao = numero.split('.')
        inverso = divisao[1].lstrip('0') + '.' + divisao[0]
        print(f'{inverso}')
    except EOFError:
        break