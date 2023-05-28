def campeao(n):
    for i in range(1, len(votos)):
        if votos[0] < votos[i]:
            return 'N'
    return 'S'

n = int(input())
votos = []
for i in range(n):
    votos.append(int(input()))

print(campeao(n))