# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)


# n = int(input())
# for a in range(1, n + 1):
#     licznik = True
#     for i in range(2, a):
#         if a % i == 0:
#             licznik = False
#     if licznik:
#         print(a)

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


x,y = str(input("1. (x/y) ")),str(input("2. (x/y) "))
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