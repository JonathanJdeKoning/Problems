from itertools import groupby
def solve():
    N = int(input())
    S = input()
    ans = 0
    for k, v in groupby(S):
        ans = max(ans, len(list(v)) +1)

    return ans



for _ in range(int(input())):
    print(solve())