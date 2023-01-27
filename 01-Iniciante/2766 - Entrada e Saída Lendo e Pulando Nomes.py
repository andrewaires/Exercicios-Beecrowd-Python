while True:
    try:
        x = []
        for i in range(10):
            x.append(input())

        print(f'{x[2]}')
        print(f'{x[6]}')
        print(f'{x[8]}')
    except EOFError:
        break
