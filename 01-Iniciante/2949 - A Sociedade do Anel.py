n = int(input())

lista = []
for i in range(n):
    nome, id = input().split()
    lista.append((nome, id))

hobbit = 0
humanos = 0
elfos = 0
anao = 0
mago = 0

for i in range(n):
    if lista[i][1] == 'X':
        hobbit += 1
    elif lista[i][1] == 'H':
        humanos += 1
    elif lista[i][1] == 'E':
        elfos += 1
    elif lista[i][1] == 'A':
        anao += 1
    else:
        mago += 1

print(f'''{hobbit} Hobbit(s)
{humanos} Humano(s)
{elfos} Elfo(s)
{anao} Anao(oes)
{mago} Mago(s)''')
