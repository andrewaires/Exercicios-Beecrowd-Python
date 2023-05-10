n = int(input())
for i in range(n):
    n_testes = int(input())
    testes = []
    for _ in range(n_testes):
        testes.append(input())

    n_formulas = int(input())
    formulas = []
    for _ in range(n_formulas):
        formulas.append(input())

    resultados = []
    for k in range(len(formulas)):
        x = False
        for j in range(len(testes)):
            if formulas[k].find(testes[j]) != -1:
                posicao = formulas[k].find(testes[j])
                frente = posicao + len(testes[j])
                if frente < len(formulas[k]):
                    ultimo = formulas[k][frente - 1]
                    proximo = formulas[k][frente]

                    if (ultimo.isdigit() and not proximo.isdigit()) or \
                            (ultimo.isupper() and proximo.isupper()) or \
                            (ultimo.islower() and proximo.isupper()):
                        resultados.append('Abortar')
                        x = True
                        break
                else:
                    x = True
                    resultados.append('Abortar')
                    break

        if x == False:
            resultados.append('Prossiga')

    for resultado in resultados:
        print(resultado)
    if i < n-1:
        print()
