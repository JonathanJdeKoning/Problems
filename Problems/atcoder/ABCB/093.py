A, B, K = list(map(int, input().split()))
good= set()

for i in range(A,min(B+1,A+K)):
    good.add(i)

for i in range(B, max(B-K, A-1), -1):
    good.add(i)

print("\n".join([str(x) for x in sorted(good)]))