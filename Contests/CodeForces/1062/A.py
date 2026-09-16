def solve():
    nums = list(map(int, input().split()))
    if len(set(nums)) == 1:
        return "YES"
    return "NO"

for _ in range(int(input())):
    print(solve())