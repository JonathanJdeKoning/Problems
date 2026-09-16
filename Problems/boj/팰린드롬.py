N = int(input())
A = list(map(int, input().split()))
Q = int(input())
good = [[0]*len(A) for _ in range(len(A))]



for i in range(len(A)):
    l = i
    r = i
    while l >= 0 and r <= len(A)-1:
        if A[l] == A[r]:
            good[l][r] = 1
            l -= 1
            r += 1
        else:
            break

for _ in range(Q):
    S, E = list(map(int, input().split()))
    print(good[S-1][E-1])