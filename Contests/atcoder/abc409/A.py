N = int(input())
T = input()
S = input()

for a,b in zip(T, S):
    if a == "o" and b == "o":
        exit(print("Yes"))
print("No")