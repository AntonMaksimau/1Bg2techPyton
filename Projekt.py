m = 0
while m != 1 and m != 2:
    m = str(input("Policzyć liczbę konkretną(1) czy wszystkie liczby do wpisanej(2)? "))
    if m == "1":
        m1 = int(input("\nKtórą liczbę policzyć? "))
        suma = 0
        for i in range(1, (m1 + 2) // 2):
            if m1 % i == 0:
                suma += i
        if suma == m1:
            print(f"\nLiczba {m1} jest liczbą doskonałą")
        else:
            print(f"\nLiczba {m1} nie jest liczbą doskonałą")
        break
    elif m == "2":
        m2 = int(input("\nDo której liczby policzyć? "))
        progr = 0
        while progr != 1 and progr != 2:
            progr = int(input("\nWypisywać progres za pomocą procentów(1) czy wyświetlania sprawdzenia dla każdej liczby osobno(2)? "))
            if progr != 1 and progr != 2:
                print("Można wpisać tylko 1 lub 2!")
        n = 0
        ilosc = 0
        proc = 0
        list = ""
        while n < m2:
            suma = 0
            check = proc
            n += 1
            if progr == 1:
                for i in range(1,101):
                    if n >= (i / 100) * m2:
                        proc = i
                if proc != check:
                    print(f"{proc}%")
            else:
                print(n)
            for i in range(1, (n + 2) // 2):
                if n % i == 0:
                    suma += i
            if suma == n:
                if progr == 2:
                    print("Tak\n")
                list = str(list) + "\n" + str(ilosc + 1) + ") " + str(n)
                ilosc += 1
            else:
                if progr == 2:
                    print("Nie\n")
        końcówka = ""
        kon = ""
        kon2 = "ych"
        if n % 10 == 1 and n % 100 != 11:
            końcówka = "y"
        if ilosc % 10 == 1 and ilosc % 100 != 11:
            kon = "a"
            kon2 = kon
        if (ilosc % 10 == 2 or ilosc % 10 == 3 or ilosc % 10 == 4) and ilosc != 12 and ilosc != 13 and ilosc != 14:
            kon = "y"
        print(f"Wśród {n} liczb{końcówka} jest {ilosc} liczb{kon} doskonał{kon2}:\n{list}")
        break
    else:
        print("\nMusiała być wpisana tylko cyfra 1 lub 2!\n")