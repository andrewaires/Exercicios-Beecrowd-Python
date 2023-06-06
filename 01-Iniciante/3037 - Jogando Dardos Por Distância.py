n = int(input())
for i in range(n):
    joao = []
    maria = []
    for j in range(3):
        x, d = map(int, input().split())
        joao.append(x * d)
    for k in range(3):
        x, d = map(int, input().split())
        maria.append(x * d)

    if sum(joao) >= sum(maria):
        print('JOAO')
    else:
        print('MARIA')
