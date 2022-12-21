### 1.0
# m = 0
# while m != 1 and m != 2:
#     m = str(input("Policzyć liczbę konkretną(1) czy wszystkie liczby do wpisanej(2)? "))
#     if m == "1":
#         m1 = int(input("\nKtórą liczbę policzyć? "))
#         suma = 0
#         for i in range(1, m1 // 2 + 1):
#             if m1 % i == 0:
#                 suma += i
#         if suma == m1:
#             print(f"\nLiczba {m1} jest liczbą doskonałą")
#         else:
#             print(f"\nLiczba {m1} nie jest liczbą doskonałą")
#         break
#     elif m == "2":
#         m2 = int(input("\nDo której liczby policzyć? "))
#         progr = 0
#         while progr != 1 and progr != 2:
#             progr = int(input("\nWypisywać progres za pomocą procentów(1) czy wyświetlania sprawdzenia dla każdej liczby osobno(2)? "))
#             if progr != 1 and progr != 2:
#                 print("Można wpisać tylko 1 lub 2!")
#         n = 0
#         ilosc = 0
#         proc = 0
#         list = ""
#         while n < m2:
#             suma = 0
#             check = proc
#             n += 1
#             if progr == 1:
#                 for i in range(1,101):
#                     if n >= (i / 100) * m2:
#                         proc = i
#                 if proc != check:
#                     print(f"{proc}%")
#             else:
#                 print(n)
#             for i in range(1, n // 2 + 1):
#                 if n % i == 0:
#                     suma += i
#             if suma == n:
#                 if progr == 2:
#                     print("Tak\n")
#                 list += "\n" + str(ilosc + 1) + ") " + str(n)
#                 ilosc += 1
#             else:
#                 if progr == 2:
#                     print("Nie\n")
#         końcówka = ""
#         kon = ""
#         kon2 = "ych"
#         if n % 10 == 1 and n % 100 != 11:
#             końcówka = "y"
#         if ilosc % 10 == 1 and ilosc % 100 != 11:
#             kon = "a"
#             kon2 = kon
#         if (ilosc % 10 == 2 or ilosc % 10 == 3 or ilosc % 10 == 4) and ilosc != 12 and ilosc != 13 and ilosc != 14:
#             kon = "y"
#         print(f"Wśród {n} liczb{końcówka} jest {ilosc} liczb{kon} doskonał{kon2}:\n{list}")
#         break
#     else:
#         print("\nMusiała być wpisana tylko cyfra 1 lub 2!\n")



### 2.0
# n = int(input("Do jakiej liczby policzyć? "))
# nilosc = 0
# max = ""
# check = 0
# proc = 0
# for a in range(1, n + 1):
#     o = a
#     ilosc = 0
#     while a != 1:
#         if a % 2 == 1:
#             a = a * 3 + 1
#             ilosc += 1
#         else:
#             a /= 2
#             ilosc += 1
#         if nilosc == ilosc:
#             max += "\n" + str(o)
#         elif nilosc < ilosc:
#             nilosc = ilosc
#             max = str(o)
#     for i in range(1,101):
#         if o >= i / 100 * n:
#             proc = i
#     if proc != check:
#         print(f"{proc}% ({o})")
#         check = proc
# print(f"\nNajwiększa ilosc kroków ({nilosc}) dają liczby:\n{max}")

### 2.1
# n = int(input())
# ilosc = 0
# while n != 1:
#     if n % 2 == 1:
#         n = n * 3 + 1
#         ilosc += 1
#         print(n)
#     else:
#         n /= 2
#         ilosc += 1
#         print(n)
# print(f"{ilosc} kroki")

### 3.0
# n = int(input())
# a = 1
# while n != 0:
#     check = True
#     a += 1
#     for b in range(2,a // 2 + 1):
#         if a % b == 0:
#             check = False
#             break
#     if check:
#         print(a)
#         n -= 1

### 4.0
# a = float(input("Liczba "))
# rt = int(input("Pierwiastek - "))
# print(a ** (1 / rt))

### 4.1
# import math
# a = int(input())
# print(math.sqrt(a))

### 5.0
# l1 = int(input())
# l2 = 0
# while l1 > 0:
#     l2 = l2 * 10 + l1 % 10
#     l1 //= 10
# print(l2)

### 6.0
# n, k = int(input()), int(input())
# last = 0
# for i in range(1, n + 1):
#     last = (last + k) % i
# print(last + 1)

### 7.0
# x,y = str(input()),str(input())
# sl = True
# a,c,b,d = int(x[0]), int(y[0]), 0, 0
# for i in range(1, len(x)):
#     if x[i] != "/" and sl:
#         a = a * 10 + int(x[i])
#     elif x[i] == "/":
#         sl = False
#     else:
#         b = b * 10 + int(x[i])
#     preb = b
#     prea = a
# sl = True
# for i in range(1, len(y)):
#     if y[i] != "/" and sl:
#         c = c * 10 + int(y[i])
#     elif y[i] == "/":
#         sl = False
#     else:
#         d = d * 10 + int(y[i])
#     pred = d
#     prec = c
# il = b * d
# while b != d:
#     if b > d : b = b - d
#     if d > b : d = d - b
# nww = il / b
# prenww = nww
# a *= nww / preb
# c *= nww / pred
# list = f"{x} + {y} = {int(a)}/{int(prenww)} + {int(c)}/{int(prenww)} = {int(a + c)}/{int(prenww)} = "
# mian = c + a
# if mian // nww >= 1:
#     cal = int(mian // nww)
#     mian -= (mian // nww) * nww
#     for i in range(1,int(nww)):
#         if nww / i % 1 == 0 and mian / i % 1 == 0:
#             nww /= i
#             mian /= i
#     if mian == 0:
#         print(f"{list}{cal}")
#     else:
#         print(f"{list}{cal} i {int(mian)}/{int(nww)}")
# else:
#     for i in range(1,int(nww)):
#         if nww / i % 1 == 0 and mian / i % 1 == 0:
#             nww /= i
#             mian /= i
#     print(f"{list}{int(mian)}/{int(nww)}")

### 7.1
# x, y = str(input()), str(input())
# a,b, c,d = 0,0, 0,0
# sl = True
# for i in range(len(x)):
#     if x[i] != "/" and sl:
#         a = a * 10 + int(x[i])
#     elif x[i] == "/":
#         sl = False
#     else:
#         b = b * 10 + int(x[i])
# sl = True
# for i in range(len(y)):
#     if y[i] != "/" and sl:
#         c = c * 10 + int(y[i])
#     elif y[i] == "/":
#         sl = False
#     else:
#         d = d * 10 + int(y[i])
# if b == 0:
#     b = 1
# if d == 0:
#     d = 1
# up = int(a * c)
# down = int(b * d)
# for i in range(min(up,down),1,-1):
#     if up % i == 0 and down % i == 0:
#         up = int(up / i)
#         down = int(down / i)
#         break
# if up > down:
#     cal = int(up // down)
#     up = int(up - (up // down) * down)
#     if up != 0:
#         print(f"{cal} i {up}/{down}")
#     else:
#         print(f"{cal}")
# elif up == down and up != 0:
#     print("1")
# else:
#     if up != 0:
#         print(f"{up}/{down}")
#     else:
        # print("0")