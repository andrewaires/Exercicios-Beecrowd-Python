import math

def primo(num):
    if num != 2 and (num % 2 == 0 or num == 1):
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True

while True:
    try:
        moedas = int(input())
    except EOFError:
        break
    vet = []
    for i in range(moedas):
        vet.append(int(input()))
    salto = int(input())
    x = 0
    i = moedas - 1
    while i >= 0:
        x += vet[i]
        i -= salto
    if primo(x):
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else:
        print("Bad boy! I’ll hit you.")
