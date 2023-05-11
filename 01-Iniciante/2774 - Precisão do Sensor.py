import math

def precisao(H, M, medidas):
    QT = (H * 60) // M
    media = sum(medidas) / len(medidas)
    soma = sum((x - media) ** 2 for x in medidas)
    precisao = math.sqrt(soma / (QT - 1))
    return "{:.5f}".format(precisao)

while True:
    try:
        H, M = map(int, input().split())
        medidas = list(map(float, input().split()))
        resultado = precisao(H, M, medidas)
        print(resultado)
    except EOFError:
        break
