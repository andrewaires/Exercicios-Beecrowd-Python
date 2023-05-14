n = int(input())
sequencia = [0] * n
for i, valor in enumerate(map(int, input().split())):
    sequencia[i] = valor

count = 1
for x in range(2, n):
    if sequencia[x] - sequencia[x - 1] != sequencia[x - 1] - sequencia[x - 2]:
        count += 1
print(count)