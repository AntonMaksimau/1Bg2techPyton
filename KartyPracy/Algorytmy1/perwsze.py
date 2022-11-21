# sprawdź czy dana liczba jest pierwsza
n = int(input())
a = 1
while n != 0:
    check = True
    a += 1
    for b in range(2,a // 2 + 1):
        if a % b == 0:
            check = False
            break
    if check:
        print(a)
        n -= 1