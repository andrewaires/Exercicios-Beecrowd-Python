x = int(input())
y = 0
j = 1
valores = []
for i in range(x):
    valores.append(j)
    y, j = j, (y+j)

valores = sorted(valores, reverse=True)
print(' '.join(str(v) for v in valores))