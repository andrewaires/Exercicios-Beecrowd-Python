e, f, c = map(int, input().split())

total = e + f
garrafas = 0

while total >= c:
    garrafas += total // c
    total = (total // c) + (total % c)

print(garrafas)
