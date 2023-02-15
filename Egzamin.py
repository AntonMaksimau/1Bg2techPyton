# Zad 1.1
# https://arkusze.pl/maturalne/informatyka-2016-maj-matura-rozszerzona.pdf
a = int(input("a = "))
b = int(input("b = "))

dzielnikia, dzielnikib = "", ""
sumadza, sumadzb = 0, 0
for i in range(1,a // 2 + 1):
    if a % i == 0:
        dzielnikia += f"{i} "
        sumadza += i
for i in range(1,b // 2 + 1):
    if b % i == 0:
        dzielnikib += f"{i} "
        sumadzb += i
print(f"Dzielniki a - {dzielnikia}\nDzielniki b - {dzielnikib}\nsuma dzielników a - {sumadza}\nsuma dzielników b - {sumadzb}")
if sumadza == b + 1 and sumadzb == a + 1:
    print("Są skojarzone")
else:
    print("Nie są skojarzone")
