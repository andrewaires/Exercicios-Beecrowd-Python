n, g = map(int, input().split())

runas = {}
for i in range(n):
    chave, valor = input().split()
    runas[chave] = int(valor)

x = int(input())
runas_recitadas = list(input().split())

amizade = 0
for i in range(len(runas_recitadas)):
    amizade += runas[runas_recitadas[i]]

if amizade >= g:
    print(amizade)
    print('You shall pass!')
else:
    print(amizade)
    print('My precioooous')
