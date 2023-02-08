letras = 'abcdefghijklmnopqrstuvwxyz'

while True:
    try:
        n = int(input())
        mensagem = ''
        for i in range(n):
            codigo = input().split()
            posicao = len(codigo[0]) + 3 * (len(codigo) - 1)
            mensagem += letras[posicao - 1]
        print('\n'.join(mensagem))
    except EOFError:
        break
