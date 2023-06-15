while True:
    try:
        h, m = map(int, input().split())
        hora = str(h // 30).zfill(2)
        minuto = str(m // 6).zfill(2)
        print(f'{hora}:{minuto}')
    except EOFError:
        break
