

def solve():
    A, B, C = list(map(int, input().split()))
    if B-A == C-B: return "YES"
    

for _ in range(int(input())):
    print(solve())