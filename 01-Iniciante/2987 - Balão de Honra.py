def posicao_letra(letra):
    posicao = ord(letra) - ord('A') + 1
    return posicao

letra = input()
print(posicao_letra(letra))