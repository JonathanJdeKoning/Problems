N, P = list(map(int, input().split()))

A = list(map(int, input().split()))

print(len([x for x in A if x < P]))