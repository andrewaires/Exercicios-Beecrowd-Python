n = int(input())
m = int(input())
album = set()
for i in range(m):
    album.add(int(input()))

resultado = n - len(album)
if resultado >= n:
    print('0')
else:
    print(resultado)

