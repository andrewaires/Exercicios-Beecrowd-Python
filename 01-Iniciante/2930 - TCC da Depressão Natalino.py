e, d = map(int, input().split())

if e > d:
    print('Eu odeio a professora!')
elif e + 3 <= d:
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')
    e += 2
    if e >= 24:
        print('Fail! Entao eh nataaaaal!')
    else:
        print('TCC Apresentado!')