# Zad 1
# x = int(input())
# suma = 0
# while x > 0:
#     suma += x % 10
#     x //= 10
# print(suma)

# Zad 2
# a = int(input())
# for i in range(2, int(a ** 0.5 + 1)):
#     if a % i == 0:
#         print("NIE")
#         exit(0)
# print("TAK")

# Zad 3
# a = int(input())
# suma = 0
# for i in range(1, a // 2 + 1):
#     if a % i == 0:
#         suma += i
# if suma == a:
#     print("TAK")
# else:
#     print("NIE")

# Zad 4
# x, y = int(input()), int(input())
# while x != y:
#     if x > y : x = x - y
#     if y > x : y = y - x
# if x == 1:
#     print("TAK")
# else:
#     print("NIE")

# Zad 5
# m = int(input())
# lista = ""
# for i in range(10,20):
#     x, y = i, m
#     while y != x:
#         if x > y : x = x - y
#         if y > x : y = y - x
#     if x == 1:
#         lista += f"{i}\n"
# print(lista)

# Zad 6
# a, b = int(input()), int(input())
# for i in range(min(a,b), 1, -1):
#     if a % i == 0 and b % i == 0:
#         a, b = a / i, b / i
# print(f"{int(a)}/{int(b)}")

# Zad 7
# a, b = int(input()), int(input())
# cal = a // b
# a -= cal * b
# for i in range(a, 1, -1):
#     if a % i == 0 and b % i == 0:
#         a, b = a / i, b / i
# print(f"{cal}  {int(a)}/{int(b)}")

# Zad 8
# def sum(x):
#     suma = 0
#     for i in range(1, x // 2 + 1):
#         if x % i == 0:
#             suma += i
#     return suma
# for a in range(1, 10001):
#     suma = sum(a)
#     if a == sum(suma) and a != suma:
#         print(f"{a}    {suma}")

# Zad 9
# list = []
# for i in range(2,101):
#     pierwsza = True
#     for a in range(2, i // 2 + 1):
#         if i % a == 0:
#             pierwsza = False
#             break
#     if pierwsza:
#         list.append(i)
# odp = []
# for a in list:
#     for b in list:
#         if a * b > 9 and a * b < 100:
#             odp.append(a * b)
# print(sorted(set(odp)))

# Zad 10
# n = int(input())
# def jest_pierwsza(x):
#     pierwsza = True
#     for i in range(2, x // 2 + 1):
#         if x % i == 0:
#             pierwsza = False
#             break
#     return pierwsza
# if jest_pierwsza(n):
#     if jest_pierwsza(n + 2):
#         print(n + 2)
#     elif jest_pierwsza(n - 2):
#         print(n - 2)
#     else:
#         print(f"liczba {n} nie ma pary liczby pierwszej")
# else:
#     print(f"{n} nie jest liczbą pierwszą")