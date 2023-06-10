def verifica_arvore(h, d, g):
    if h >= 200 and h <= 300 and d >= 50 and g >= 150:
        return 'Sim'
    return 'Nao'

n = int(input())
for i in range(n):
    h, d, g = map(int, input().split())
    print(verifica_arvore(h, d, g))