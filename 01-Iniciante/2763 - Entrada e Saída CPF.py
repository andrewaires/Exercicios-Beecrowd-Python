while True:
    try:
        cpf = input().split('.')
        dd = cpf[2].split('-')
        for i in cpf[:-1]:
            print(i)
        for _ in dd:
            print(_)
    except EOFError:
        break