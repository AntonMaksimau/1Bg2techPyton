# Zad 1
# def suma():
#     suma = 0
#     for i in range(10,100):
#         pierwsza = True
#         for j in range(2,i // 2 + 1):
#             if i % j == 0:
#                 pierwsza = False
#                 break
#         if pierwsza:
#             suma += i
#     return suma
# print(suma())

# Zad 2
# def suma_cyfr(liczba, pierwiastek):
#     iloczyn = liczba ** pierwiastek
#     suma = 0
#     while iloczyn > 0:
#         suma += iloczyn % 10
#         iloczyn //= 10
#     return suma
# print(suma_cyfr(2,2019))

# Zad 3
# n = int(input())
# def lista_boków_trójkątów(x):
#     list = []
#     for a in range(1, x):
#         for b in range(a, x):
#             c = (a ** 2 + b ** 2) ** 0.5
#             if a + b + c == x and c == int(c):
#                 list.append((a, b, int(c)))
#     return list
# print(lista_boków_trójkątów(n))

# Zad 4
# def dzielnik(n, d):
#     return n % d == 0
# a, b = int(input()), int(input())
# print(dzielnik(a, b))

# Zad 5
# def suma_cyfr(x):
#     suma = 0
#     while x > 0:
#         suma += x % 10
#         x //= 10
#     return suma
# n = int(input())
# print(suma_cyfr(n))

# Zad 6
# Wersja 1
# def pierwsza(n):
#     if n % 2 == 0:
#         return druga(n)
#     else:
#         return trzecia(n)
# def druga(n):
#     return n * 3
# def trzecia(n):
#     return n * 0.4
# Wersja 2
