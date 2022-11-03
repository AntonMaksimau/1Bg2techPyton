# Zad 1 - Medium - Oblicz sumę k  początkowych liczb trzycyfrowych
# k = int(input())
# a = 0
# b = 100
# for i in range(k):
#     a += b
#     b += 1
# print(a)

# Zad 2 - Hard - Oblicz sumę n początkowych wyrazów w ciągu fibonacciego
# n = int(input())
# a = 0
# b = 1
# suma = 0
# for i in range (n):
#     suma += a
#     a,b = b, a + b
# print(suma)

# Zad 3 - Hard - Sprawdź czy liczba wpisana przez usera jest doskonałą
# n = int(input())
# suma = 0
# for i in range(1,n):
#     if n % i == 0:
#         suma += i
# if suma == n:
#     print("Tak")
# else:
#     print("Nie")

# Zad 3.2
# n = 0
# while True:
#     suma = 0
#     n += 1
#     print(n)
#     for i in range(1,n):
#         if n % i == 0:
#             suma += i
#     if suma == n:
#         print("Tak\n")
#     else:
#         print("Nie\n")

# Zad 4 - Medium - Oblicz sumnę liczb dwucyfrowych podzielnych przez 7
# suma = 0
# for i in range(10,100):
#     if i % 7 == 0:
#         suma += i
# print(suma)