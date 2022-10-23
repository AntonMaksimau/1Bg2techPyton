# Zad 1 
k,l,m = int(input("k = ")),int(input("l = ")),int(input("m = "))
if k == l and k != m and l != m:
    print(f"k = l ({k})")
elif k == m and k != l and l != m:
    print(f"k = m ({k})")
elif l == m and l != k and m != k:
    print(f"l = m ({l})")
else:
    print("Wszystkie liczby są różne albo równe")