while True:
    try:
        n = int(input())
        tempo = []
        for i in range(n):
            tempo.append(float(input()))

        resultado = tempo[0]
        for i in range(1, len(tempo)):
            if tempo[i] < resultado:
                resultado = tempo[i]
        print(f'{resultado:.2f}')

    except EOFError:
        break
