posicao, destino = input().split()
diferenca_coluna = abs(ord(destino[0]) - ord(posicao[0]))
diferenca_linha = abs(int(destino[1]) - int(posicao[1]))

if (diferenca_linha == 1 and diferenca_coluna == 2) or (diferenca_linha == 2 and diferenca_coluna == 1):
    print('VALIDO')
else:
    print('INVALIDO')