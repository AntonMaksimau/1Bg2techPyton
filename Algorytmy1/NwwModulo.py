# NWW
a,b = float(input()), float(input())
il = a * b
while b > 0:
    a, b = b, a % b
print(il / a)