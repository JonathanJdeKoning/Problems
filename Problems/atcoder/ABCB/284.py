T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(1 for x in A if x%2==1))
