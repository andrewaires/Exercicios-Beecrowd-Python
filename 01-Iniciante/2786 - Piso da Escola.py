largura = int(input())
comprimento = int(input())

lajota_tipo_1 = largura * comprimento
lajota_tipo_1 += (largura-1) * (comprimento-1)

lajota_tipo_2 = ((largura - 1) + (comprimento - 1)) * 2

print(lajota_tipo_1)
print(lajota_tipo_2)