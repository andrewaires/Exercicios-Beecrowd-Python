feijoes = list(map(int, input().split()))

for i in range(len(feijoes)):
    if feijoes[i] == 1:
        print(i+1)
