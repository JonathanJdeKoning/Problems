N = int(input())

seen = set()

for _ in range(N):
    seq = list(map(int, input().split()))
    seq = tuple(seq)
    seen.add(seq)

print(len(seen))