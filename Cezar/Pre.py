# Funkcja ord() - zwraca kod ASCII danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# Funkcja chr() - zwraca znak danego kodu ASCII (odwrotność ord())
# print(chr(65))
# print(chr(75))
# print(chr(89))

# Znaki ASCII od A-Z mają kody 65 - 90

# Wypisz pętlą for cały alfabet A-Z
# for i in range(65,91):
#     print(chr(i), end=" ")

# Jak słowo rozbić na litery?
# napis = "POLSKA"
# print(len(napis)) # zwraca długość napisu
# print(napis[0]) # napis to lista
# print(napis[1])
# print(napis[2])

# Wypiszcie kody ASCII literek napisu
# napis = "POLSKA"
# for i in range(len(napis)):
#     print(chr(65 + (ord(napis[i]) - 65 + 3) % 26))

# napis = str(input())
# for i in range(len(napis)):
#     print(chr(65 + (ord(napis[i]) - 65 + 3) % 26))

# a,b,c,d = int(input()),int(input()),int(input()),int(input())
# preb = b
# pred = d
# il = b * d
# while b != d:
#     if b > d : b = b - d
#     if d > b : d = d - b
# nww = il // b
# a = a * (nww // preb)
# c = c * (nww // pred)
# odp = c + a
# print(f"{odp}/{nww}")


x,y = str(input()),str(input())
sl = True
a,c,b,d = int(x[0]), int(y[0]), 0, 0
for i in range(1, len(x)):
    if x[i] != "/" and sl:
        a = a * 10 + int(x[i])
    elif x[i] == "/":
        sl = False
    else:
        b = b * 10 + int(x[i])
    preb = b
    prea = a
sl = True
for i in range(1, len(y)):
    if y[i] != "/" and sl:
        c = c * 10 + int(y[i])
    elif y[i] == "/":
        sl = False
    else:
        d = d * 10 + int(y[i])
    pred = d
    prec = c
il = b * d
while b != d:
    if b > d : b = b - d
    if d > b : d = d - b
nww = il / b
prenww = nww
a *= nww / preb
c *= nww / pred
list = f"{x} + {y} = {int(a)}/{int(prenww)} + {int(c)}/{int(prenww)} = {int(a + c)}/{int(prenww)} = "
mian = c + a
if mian // nww >= 1:
    cal = int(mian // nww)
    mian -= (mian // nww) * nww
    for i in range(1,int(nww)):
        if nww / i % 1 == 0 and mian / i % 1 == 0:
            nww /= i
            mian /= i
    if mian == 0:
        print(f"{list}{cal}")
    else:
        print(f"{list}{cal} i {int(mian)}/{int(nww)}")
else:
    for i in range(1,int(nww)):
        if nww / i % 1 == 0 and mian / i % 1 == 0:
            nww /= i
            mian /= i
    print(f"{list}{int(mian)}/{int(nww)}")