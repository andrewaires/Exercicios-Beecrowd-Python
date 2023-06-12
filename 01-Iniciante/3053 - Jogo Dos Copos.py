n = int(input())
posicao = input()

for i in range(n):
    movimento = int(input())
    if movimento == 1:
        if posicao == 'A':
            posicao = 'B'
        elif posicao == 'B':
            posicao = 'A'
    elif movimento == 2:
        if posicao == 'B':
            posicao = 'C'
        elif posicao == 'C':
            posicao = 'B'
    else:
        if posicao == 'C':
            posicao = 'A'
        elif posicao == 'A':
            posicao = 'C'
print(posicao)
