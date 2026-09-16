
def solve():
    a,b,c,d = list(map(int, input().split()))
    a,b = sorted([a,b])
    if (c > a and c < b) ^ (d > a and d < b):
        return "YES"
    return "NO"


for _ in range(int(input())):
    print(solve())