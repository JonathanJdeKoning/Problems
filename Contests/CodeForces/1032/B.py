def solve():
    N = int(input())
    S = input()
    mid = S[1:-1]
    if len(set(list(mid))) != len(mid):
        return "Yes"
    if S[0] in mid or S[-1] in mid:
        return "Yes"
    return "No"

for _ in range(int(input())):
    print(solve())