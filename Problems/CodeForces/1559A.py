from functools import reduce
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    return reduce(lambda a,b: a&b, A)



for _ in range(int(input())):
    print(solve())