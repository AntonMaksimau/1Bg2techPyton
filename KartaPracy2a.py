# Zad 1
# a,b = int(input()),int(input())
# if (a + b) % 2 == 0:
#     print("tak")
# else:
#     print("nie")

# Zad 2
# a,g = int(input()),int(input())
# if (a + g) / 2 > (a * g) ** 0.5:
#     print("tak")
# else:
#     print("nie")

# Zad 3
# k,l,m = int(input("k = ")),int(input("l = ")),int(input("m = "))
# if k == l and l != m and k != m:
#     print("\nk = l")
# elif k == m and l != m and l != k:
#     print("\nk = m")
# elif m == l and k != m and k != l:
#     print("\nm = l")
# else:
#     print("\nNie")

# Zad 4
# a,b,c,d = int(input("a = ")),int(input("b = ")),int(input("c = ")),int(input("d = "))
# if a < b and a < c and a < d:
#     print("\nNajmniejsza liczba to a(" + str(a) + ")")
# elif b < a and b < c and b < d:
#     print("\nNajmniejsza liczba to b(" + str(b) + ")")
# elif c < a and c < b and c < d:
#     print("\nNajmniejsza liczba to c(" + str(c) + ")")
# elif d < b and d < c and d < a:
#     print("\nNajmniejsza liczba to d(" + str(d) + ")")
# else:
#     print("\nTu nie ma najmniejszej liczby")

# Zad 5
# a,b,c = int(input("a = ")),int(input("b = ")),int(input("c = "))
# if a + b > c and b + c > a and c + a > b:
#     print("Tak")
# else:
#     print("Nie")

# Zad 6
# a,b,c = int(input("a = ")),int(input("b = ")),int(input("c = "))
# if a ** 2 == b ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2 or b ** 2 == a ** 2 + c ** 2:
#     print("Trókąt jest prostokątnym")
# elif a ** 2 > b ** 2 + c ** 2 or c ** 2 > b ** 2 + a ** 2 or b ** 2 > a ** 2 + c ** 2:
#     print("Trójkąt jest rozwartokątnym")
# elif a ** 2 < b ** 2 + c ** 2 or c ** 2 < b ** 2 + a ** 2 or b ** 2 < a ** 2 + c ** 2:
#     print("Trókąt jest ostrokątnym")
