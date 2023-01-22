x = int(input())
for i in range(x):
    energia = int(input())
    if energia <= 8000:
        print('Inseto!')
    else:
        print('Mais de 8000!')