def domino(n):
    n_pecas = int((n + 1) * (n + 2) / 2)
    return n_pecas

n = int(input())
print(domino(n))
