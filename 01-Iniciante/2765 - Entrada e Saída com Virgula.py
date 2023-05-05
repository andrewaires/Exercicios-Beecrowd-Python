while True:
    try:
        entrada = input().split(',')
        print(f'{entrada[0]}')
        print(f'{entrada[1]}')
    except EOFError:
        break


