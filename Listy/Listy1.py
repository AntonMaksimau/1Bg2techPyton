L = [7,3,8,5,6]
# print(L[1])
# print(len(L))
# print(L)

# for elem in L:
#     print(elem, end = " ")
# print("\n")

# for i in range(len(L)):
#     print(L[i], end = " ")
# print("\n")

print(L)
L.append(4)
L.append(5)
print(L)
print(L.count(5))
print(L.index(5))
L.reverse()
print(L)
L.sort()
print(L)
L = set(L)
print(L)
print(max(L))
print(min(L))