# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

# n = int(input())
# for a in range(1,n+1):
#     licznik = True
#     for i in range(2,a):
#         if a % i == 0:
#             licznik = False
#     if licznik:
#         print(a)

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
                