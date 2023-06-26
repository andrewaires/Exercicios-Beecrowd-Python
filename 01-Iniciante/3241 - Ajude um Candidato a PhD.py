n = int(input())

resultado = []
for i in range(n):
    entrada = list(input().split('+'))

    if len(entrada) == 1:
        resultado.append('skipped')
    else:
        resultado.append(int(entrada[0]) + int(entrada[1]))

for i in resultado:
    print(i)