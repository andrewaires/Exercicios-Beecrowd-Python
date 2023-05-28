n = int(input())
gasto = 0
verba = 0
for i in range(n):
    t, c = input().split()
    if t == 'G':
        gasto += int(c)
    else:
        verba += int(c)

if gasto > verba:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')