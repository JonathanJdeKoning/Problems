def solve():
    N = int(input())
    if (N**0.5).is_integer():
        return f"{0} {int(N**0.5)}"
    return -1

            
for _ in range(int(input())):
    print(solve())