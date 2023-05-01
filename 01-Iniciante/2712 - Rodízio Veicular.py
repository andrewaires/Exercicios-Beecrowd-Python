n = int(input())

for i in range(n):
    placa = input()

    if len(placa) == 8 and placa[:3].isupper() and placa[:3].isalpha() and (placa[3] == '-') and placa[4:].isdigit():
        r = int(placa[7])
        if r > 8 or r == 0:
            print('FRIDAY')
        elif r > 6:
            print('THURSDAY')
        elif r > 4:
            print('WEDNESDAY')
        elif r > 2:
            print('TUESDAY')
        else:
            print('MONDAY')
    else:
        print('FAILURE')
