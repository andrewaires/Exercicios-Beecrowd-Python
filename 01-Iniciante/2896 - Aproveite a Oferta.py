t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n < k:
        print(n)
    else:
        garrafas = n // k
        resultado = n % k + garrafas
        print(resultado)