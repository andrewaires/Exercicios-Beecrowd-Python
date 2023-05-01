def trocar_lampadas(decimal):
    binario = bin(decimal)[2:]
    qtd_trocas = 0
    qtd_consecutivas = 0
    for digito in binario:
        if digito == '1':
            qtd_consecutivas += 1
            qtd_trocas = max(qtd_trocas, qtd_consecutivas)
        else:
            qtd_consecutivas = 0
    return qtd_trocas

n = int(input())

for i in range(n):
    decimal = int(input())
    qtd_trocas = trocar_lampadas(decimal)
    print(qtd_trocas)
