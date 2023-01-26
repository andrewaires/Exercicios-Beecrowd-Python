while True:
    try:
        x, y, m = map(int, input().split())
        pci = []
        for i in range(m):
            x1, x2 = map(int, input().split())
            if (x1 <= x and x2 <= y) or (x1 <= y and x2 <= x):
                pci.append('Sim')
            else:
                pci.append('Nao')

        for i in pci:
            print(i)
    except EOFError:
        break