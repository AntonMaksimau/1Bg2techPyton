# 1. Sprawdź czy dana liczba jest pierwsza
# n = int(input())
# for i in range(2,n):
#     if n % i == 0:
#         print("Nie jest pierwszą")
#         exit(0)
# print("Tak, jest pierwszą")

# 2. Generowanie liczb pierwszych (w przedziale [p,q])
# p, q = int(input()), int(input())
# for j in range(p, q + 1):
#     flaga = True
#     for i in range(2, j):
#         if j % i == 0:
#             flaga = False
#             break
#     if flaga:
#         print(j, end=" ")

# 3. Generowanie liczb pierwszych (pierwsze n liczb pierwszych)
# n = int(input("Ile liczb pierwszych wypisać? "))
# k = 2
# ilosc = 0
# while 1:
#     flaga = True
#     for i in range(2, k):
#         if k % i == 0:
#             flaga = False
#             break
#     if flaga:
#         print(k, end=" ")
#         ilosc += 1
#     if ilosc == n:
#         break
#     k += 1