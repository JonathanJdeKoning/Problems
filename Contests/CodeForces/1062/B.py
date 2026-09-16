from collections import Counter
def solve():
    N = int(input())
    S, T = input().split()
    if sorted(S) == sorted(T):
        return "YES"
    return "NO"

for _ in range(int(input())):
    print(solve())