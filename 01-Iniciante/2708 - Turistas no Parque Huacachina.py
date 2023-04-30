turistas = 0
jipes = 0
while True:
    entrada = input().split()
    if entrada[0] == 'ABEND':
        print(turistas)
        print(abs(jipes))
        break

    movimento = entrada[0]
    t = int(entrada[1])

    if movimento == 'SALIDA':
        turistas += t
        jipes -= 1
    elif movimento == 'VUELTA':
        turistas -= t
        jipes += 1