from heapq import heappush, heappop
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    def cond(n):
        

    low = 0
    high = sum(C)
    while low < high:
        mid = (low+high) // 2
        if cond(mid):
            mid = high
        else:
            mid = low+1
    return low





for _ in range(int(input())):
    print(solve())