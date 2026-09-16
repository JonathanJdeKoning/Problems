S = list(input())
T = list(input())


for i in range(27):
    S = [chr((ord(c)-96)%26+97) for c in S]
    if S == T:
        exit(print("Yes"))
print("No")