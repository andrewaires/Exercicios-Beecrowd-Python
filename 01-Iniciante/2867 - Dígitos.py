def digitos(c):
    resultado = []
    for i in range(c):
        n, m = map(int, input().split())
        potencia = str(n**m)
        print(len(potencia))

c = int(input())
digitos(c)
