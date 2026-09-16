from heapq import heappush, heappop
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

seen = set()
mathHeap = []
engHeap = []
totHeap = []

for i, (M,E) in enumerate(zip(A, B), start=1):
    heappush(mathHeap, (-M, i))
    heappush(engHeap,(-E, i))
    heappush(totHeap, (-(E+M), i))


for _ in range(X):
    score, id = heappop(mathHeap)
    seen.add(id)

while Y:
    score, id = heappop(engHeap)
    if id in seen: continue
    seen.add(id)
    Y -= 1

while Z:
    score, id = heappop(totHeap)
    if id in seen: continue
    seen.add(id)

    Z -= 1

print("\n".join(map(str, sorted(seen))))
