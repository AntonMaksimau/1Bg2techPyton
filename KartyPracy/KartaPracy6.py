# Zad 1
# a, b, c = int(input()),int(input()),int(input())
# if c - b == b - a:
#     print("Ciąg jest arytmetyczny")
# else:
#     print("Ciąg nie jest arytmetyczny")
# if c / b == b / a:
#     print("Ciąg jest geometryczny")
# else:
#     print("Ciąg nie jest geometrycznym")
# if c > b and c > a and b > a:
#     print("Ciąg jest rosnący")
# elif c < b and c <  a and b < a:
#     print("ciąg jest malejący")

# Zad 2
# sum = 0
# for i in range(100,1000):
#     if i % 8 == 0 and i % 16 != 0:
#         sum += i
# print(sum)

# Zad 3
# for i in range(10, 100):
#     if i % 7 == 0:
#         wielokrotnosc = i
# ilosc = 0
# for i in range(1000, 10000):
#     if i % wielokrotnosc == 0:
#         ilosc += 1
# print(ilosc)
        
# Zad 4
# ilosc = 0
# for i in range(10, 100):
#     if 2 * (i % 10) <= i // 10:
#         ilosc += 1
# print(ilosc)   

# Zad 5
# suma = 0
# ilosc = 0
# for i in range(100,1000):
#     if i // 100 > (i // 10) % 10 + (i % 10):
#         suma += i
#         ilosc += 1
# print(f'suma - {suma}\nilosc - {ilosc}')

# Zad 6
# n = int(input())
# suma = 0
# for i in range(1, n + 1):
#     if i < 6:
#         suma += i * 19
# print(suma)

# Zad 7
# n = int(input())
# suma = 0
# i = 999
# while n > 0:
#     if i % 37 == 0:
#         suma += i
#         n -= 1
#     i -= 1
# print(suma)

# Zad 8
# n = int(input())
# x = 5
# suma = 2
# for i in range(n - 1):
#     suma -= x
#     x = (abs(x) + 3) * (-1) ** (i + 1)
# print(suma)

# Zad 9
# n = int(input())
# il = 1
# x = 1
# for i in range(n):
#     il = il * x
#     x *= -2
# print(il)

# Zad 10
# n = int(input())
# suma = 0
# for i in range(n):
#     il = 1
#     for i in range(1, i + 2):
#         il = il * i
#     suma += il
# print(suma)

# Zad 11
# n = int(input())
# a = 1
# suma = 0
# for i in range(1, n + 1):
#     b = i * i
#     suma += a/b
#     a += 2
# print(suma)

# Zad 12
# n = int(input())
# a = 1
# suma = 0
# sumb = 0
# for i in range(1, n + 1):
#     suma += a
#     a += 2
#     b = i * i
#     sumb += b
# print(suma/sumb)

# Zad 13
# n = int(input())
# a = 2
# suma = 0
# for i in range(1, n + 1):
#     b = i ** 3 + 2
#     suma += a/b
#     a += 2
# print(suma)

# Zad 14
# n = int(input())
# a = 2
# suma = 0
# for i in range(1, n + 1):
#     b = i ** 3 + 2
#     suma += a/b
#     a += 2
# print(suma)

# Zad 15
# n = int(input())
# a = 3
# b = 1
# il = 1
# for i in range(n):
#     il *= a/b
#     a += 1
#     b = b * 2 + 1
# print(il)

# Zad 16
# n = int(input())
# a1 = 1
# a2 = 2
# b = 1
# il = 1
# for i in range(1, n + 1):
#     il *= a1/b
#     a1, a2 = a2, a1 + a2
#     b *= 2
# print(il)
