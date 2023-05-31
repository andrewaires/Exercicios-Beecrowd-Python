import math

voltas, placas = map(int, input().split())
total_voltas = voltas * placas

porcentagem = 10
matriz = []
for i in range(9):
    matriz.append(math.ceil(porcentagem * total_voltas / 100))
    porcentagem += 10

matriz_formatada = ' '.join(map(str, matriz))
print(matriz_formatada)

