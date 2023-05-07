def sugestoes(palavras_pesquisadas, consultas):
    resultado = []
    for consulta in consultas:
        sugestoes = []
        max_comprimento = -1
        for palavra in palavras_pesquisadas:
            if palavra.startswith(consulta):
                sugestoes.append(palavra)
                max_comprimento = max(max_comprimento, len(palavra))
        if sugestoes:
            resultado.append((len(sugestoes), max_comprimento))
        else:
            resultado.append((-1, -1))
    return resultado

while True:
    try:
        n = int(input())
        palavras_pesquisadas = [input().strip() for _ in range(n)]
        q = int(input())
        consultas = [input().strip() for _ in range(q)]

        resultado = sugestoes(palavras_pesquisadas, consultas)

        for sugestao in resultado:
            if sugestao[0] == -1:
                print(sugestao[0])
            else:
                print(sugestao[0], sugestao[1])
    except EOFError:
        break
