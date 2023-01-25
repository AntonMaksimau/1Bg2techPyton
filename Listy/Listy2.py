# Wygeneruj tablicę n losowych liczb:
# from random import randint
# L = [randint(1,20) for i in range(20)]



#1. Znajdź największą liczbę w tablicy
#2. Znajdź najmniejszą liczbę w tablicy
#3. Podaj ile razy występuje najwieksza liczba w tablicy
#4. Podaj ile razy występuje najmniejsza liczba w tablicy
#5. Podaj rozpiętość tablicy (różnica max - min)
#6. Podaj sumę liczb w tablicy
#7. Podaj średnią wartość liczb w tablicy
#8. Których liczb jest więcej w tablicy: parzystych czy nieparzystych?
#9. Ile w tablicy jest liczb pierwszych?
#10. Podaj v-ce max i v-ce min liczb tablicy

from random import randint
L = [randint(1,20) for i in range(20)]

print(f"Lista: {L}")

# Zad 1
print(max(L))

# Zad 2
print(min(L))

# Zad 3
print(L.count(max(L)))

# Zad 4
print(L.count(min(L)))

# Zad 5
print(max(L) - min(L))

# Zad 6
print(sum(L))

# Zad 7
print(sum(L) / len(L))

# Zad 8
sump = 0
sumn = 0
for i in L:
    if i % 2 == 0:
        sump += 1
    else:
        sumn += 1
if sumn > sump:
    print("Nieparzystych jest więcej")
elif sump == sumn:
    print("Nieparzystych jest tyle samo co parzystych")
else:
    print("Parzystych jest więcej")

# Zad 9
suma = 0
for i in L:
    pierwsza = True
    for a in range(2, i):
        if i % a == 0:
            pierwsza = False
            break
    if pierwsza:
        suma += 1
print(suma - L.count(1))