T, A, Z = map(int, input().split())

if A*Z == T: exit(print("Yes"))
while T/Z > A:
    T += 1
    A += 1
    if A*Z == T: exit(print("Yes"))
print("No")

