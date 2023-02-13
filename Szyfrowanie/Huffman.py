W = str(input())
W = W + "."
# 5M3A4RE2C3ZE2K

print(W[8])
print(len(W))

ilość = 1
H = ""
for i in range(len(W) - 1):
    if W[i] == W[i+1]:
        ilość += 1
    else:
        if ilość > 1:
            H += f"{ilość}"
        H += f"{W[i]}"
        ilość = 1
print(H)