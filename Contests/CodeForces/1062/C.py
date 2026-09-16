def solve():
    N = int(input())
    A = list(map(int, input().split()))
    odds = []
    eves = []
    for num in A:
        if num %2 == 0:
            eves.append(num)
        else:
            odds.append(num)
    if not odds or not eves:
        return " ".join(map(str, A))
    else:
        return " ".join(map(str, sorted(A)))
for _ in range(int(input())):
    print(solve())