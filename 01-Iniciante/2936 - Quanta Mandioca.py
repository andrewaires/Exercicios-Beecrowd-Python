quantidades = {
    0: 300,
    1: 1500,
    2: 600,
    3: 1000,
    4: 150,
    }

porcao = []
for i in range(5):
    porcao.append(int(input()))

mandioca_total = 0
for i in range(5):
    mandioca_total += porcao[i]*quantidades[i]

print(mandioca_total+225)