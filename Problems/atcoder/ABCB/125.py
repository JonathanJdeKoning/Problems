N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

print(sum([v-c for v, c in zip(V,C) if v-c > 0]))