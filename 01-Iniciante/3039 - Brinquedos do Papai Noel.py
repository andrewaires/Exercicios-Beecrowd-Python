n = int(input())
menino = 0
menina = 0
for i in range(n):
    nome, sexo = input().split()
    if sexo == 'M':
        menino += 1
    else:
        menina += 1
print(f'{menino} carrinhos')
print(f'{menina} bonecas')