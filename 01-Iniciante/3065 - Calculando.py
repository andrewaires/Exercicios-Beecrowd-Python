m = int(input())

teste = 1
while m > 0:
    entrada = input().split('+')
    entrada = [list(map(int, num.split('-'))) for num in entrada]
    soma = [sum(x[1:]) - x[0] for x in entrada]
    resultado = sum(soma)

    if resultado <= 0:
        resultado = abs(resultado)
    else:
        resultado -= 2 * resultado

    print(f'Teste {teste}')
    print(resultado)
    print()
    teste += 1

    m = int(input())