pontos = {
    range(0, 801): 1,
    range(801, 1401): 2,
    range(1401, 2001): 3,
}

x = int(input())
for intervalo, valor in pontos.items():
    if x in intervalo:
        print(valor)
        break
