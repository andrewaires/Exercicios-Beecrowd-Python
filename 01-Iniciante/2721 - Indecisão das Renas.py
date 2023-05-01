bolas = list(map(int, input().split()))
soma = sum(bolas)

renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

count = 0
while soma > 0:
    count = (count + 1) % 9
    soma -= 1

print(renas[count-1])
