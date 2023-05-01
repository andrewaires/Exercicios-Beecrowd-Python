def tempo(n):
    if a + b > n:
        return 'Deixa para amanha!'
    else:
        return 'Farei hoje!'


n = int(input())
a, b = map(int, input().split())
print(tempo(n))