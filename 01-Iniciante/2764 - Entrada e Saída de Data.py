while True:
    try:
        data = input().split('/')
        dia, mes, ano = data[0], data[1], data[2]
        print(f'{mes}/{dia}/{ano}')
        print(f'{ano}/{mes}/{dia}')
        print(f'{dia}-{mes}-{ano}')
    except EOFError:
        break