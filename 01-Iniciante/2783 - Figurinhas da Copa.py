N, C, M = map(int, input().split())
carimbadas = set(map(int, input().split()))
compradas = set(map(int, input().split()))

faltam = len(carimbadas - compradas)

print(faltam)
