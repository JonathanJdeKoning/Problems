A, B = input().split()

mx = max(len(A), len(B))
A = A.rjust(mx, "0")
B = B.rjust(mx, "0")

for a,b in zip(A, B):
    if int(a) + int(b) >= 10:
        exit(print("Hard"))
print("Easy")