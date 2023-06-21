import math
while True:
    try:
        n = int(input())
        seculo = math.ceil(n / 100)
        print(seculo)

    except EOFError:
        break