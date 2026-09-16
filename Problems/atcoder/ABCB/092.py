N = int(input())
D, R = list(map(int, input().split()))
E = 0
for _ in range(N):
    P = int(input())
    for i in range(1, D+1):
        if (i-1)%P == 0:
            E += 1
print(R + E)