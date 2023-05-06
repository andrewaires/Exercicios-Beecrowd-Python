elementos = {
    'fire': {
        'dano': 200,
        1: 20,
        2: 30,
        3: 50,
    },
    'water': {
        'dano': 300,
        1: 10,
        2: 25,
        3: 40,
    },
    'earth': {
        'dano': 400,
        1: 25,
        2: 55,
        3: 70,
    },
    'air': {
        'dano': 100,
        1: 18,
        2: 38,
        3: 60,
    },
}

def intercessao(x1, y1, raio, x0, y0, largura, altura):
    cDx = abs(x1 - (x0 + largura / 2))
    cDy = abs(y1 - (y0 + altura / 2))

    if (cDx > (largura / 2 + raio)) or (cDy > (altura / 2 + raio)):
        return False
    elif (cDx <= largura / 2) or (cDy <= altura / 2):
        return True
    else:
        return ((cDx - largura/2)**2 + (cDy - altura/2)**2) <= raio**2


t = int(input())
for i in range(t):
    largura, altura, x0, y0 = map(int, input().split())
    magia, nivel, x1, y1 = input().split()
    nivel = int(nivel)
    x1 = int(x1)
    y1 = int(y1)
    raio = elementos[magia][nivel]

    if intercessao(x1, y1, raio, x0, y0, largura, altura):
        print(elementos[magia]['dano'])
    else:
        print(0)
