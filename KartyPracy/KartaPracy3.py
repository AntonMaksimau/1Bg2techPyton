
# Pre
# pętla liczb dwucyfrowych od 10 do 21
# for i in range(10,22):
#    print(i, end=" ")
# pętla liczb dwucyfrowych nieparzystych od 15 do 31  
# for i in range(15,32,2):
#     print(i, end =" ")
# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1):
#     print(i,end="")
# pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,100,1):
#     print(109 - i, end=" ")
# pętla liczb 3-cyfrowych podzielnych przez 20 
# for i in range(100,1000,20):
#     print(i, end=" ")

# Zad 1
# n = int(input())
# for i in range(n):
#     print(i**3 + 3, end=" ")

# Zad 2
# for i in range(105,1000,15):
#     print(i, end=" ")

# Pre 2

# Pętle for liczb trzycyfrowych podzielnych przez 13
# for i in range(100,1000):
#     if i % 13 == 0:
#         print(i, end=" ")

# Pętle for liczb dwucyfrowyh parzystych
# for i in range(10,100,2):
#     print(i)

# Pętle for potęg cyfr: 0, 1, 4, 9, 16 .. 81
# for i in range(0,10):
#     print(f"{i} ^ 2 = {i ** 2}")

# Zad 3
# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# Zad 4
# a = 0
# for i in range(10,100):
#     a += i
# print(a)

# Zad 5
# n = int(input())
# suma = n * (n+1) // 2
# for i in range(n-1):
#     k = int(input())
#     suma -= k
# print(suma - k)

# Zad 6
# a,b = 0,1
# n = int(input())
# print(f"{a}\n{b}")
# for i in range(1,n + 1):
#     if i == a + b:
#         print(i)
#         a,b = b,i

# Zad 6.2
# a,b = 0,1
# n = int(input())
# for i in range(n):
#     print(a)
#     a,b = b, a + b