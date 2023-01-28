def is_fibo(n):
    a, b = 1, 1
    while n >= b:
        if n == b:
            return True
        a, b = b, a + b
    return False

k = int(input())
count = 0
num = 0
while count < k:
    num += 1
    if not is_fibo(num):
        count += 1
print(num)