def fib(n):
    x, y = 0,1
    for _ in range(n):
        x, y = y, x+y
    return y

def solve():
    N, M = list(map(int, input().split()))
    bigBox, smallBox = fib(N), fib(N-1)

    ans = []
    for _ in range(M):
        w, l, h = list(map(int, input().split()))

        if min(w, l, h) < bigBox:
            ans.append(0)
            continue

        w -= bigBox 
        l -= bigBox
        h -= bigBox
        
        ans.append(int(max(w, l ,h) >= smallBox))

    return "".join(map(str, ans))

for _ in range(int(input())):
    print(solve())