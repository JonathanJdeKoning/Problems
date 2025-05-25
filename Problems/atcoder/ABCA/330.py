n, l = map(int, input().split())
p = list(map(int, input().split()))
print(len([d for d in p if d>=l]))
