import struct
while True:
    try:
        a, b, c, d = input().split(maxsplit=3)
        a = int(a)
        b = struct.unpack('f', struct.pack('f', float(b)))[0]

        print(f'{a}{b:.6f}{c}{d}')
        print(f'{a}\t{b:.6f}\t{c}\t{d}')
        print('%10d%10.6f%10s%10s' % (a, b, c, d))
    except EOFError:
        break
