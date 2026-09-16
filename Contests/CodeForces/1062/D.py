from math import gcd
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    seen = set()
    mn = int(1e18)
    for num in A:
        if num in seen: continue
        for div in range(2, mn):
            if gcd(div, num) == 1:
                mn = div
                seen.add(num)
                break
    return mn
    


for _ in range(int(input())):
    print(solve())