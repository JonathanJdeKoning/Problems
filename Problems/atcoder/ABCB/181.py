N = int(input())
tot = 0

def upto(n):
    return (n*(n+1)) // 2
for _ in range(N):
    A, B = list(map(int, input().split()))

    tot += upto(B) - upto(A-1)

print(tot)
    

