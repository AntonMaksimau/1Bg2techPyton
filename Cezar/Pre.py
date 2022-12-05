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

# napis = "KOZA"
# klucz = int(input("Jaki klucz? "))
# for i in range(len(napis)):
#     print(chr(65 + (ord(napis[i]) - 65 + klucz) % 26))
