def solve():
    N, X = list(map(int, input().split()))
    
    A = list(map(int, input().split()))
    
    l = A.index(1)
    r = len(A) - A[-1::-1].index(1) - 1

    if r - l + 1 <= X:
        return "YES"
    else:
        return "NO"



for _ in range(int(input())):
    print(solve())