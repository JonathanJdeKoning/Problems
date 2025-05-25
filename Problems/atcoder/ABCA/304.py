n = int(input())

peeps = []
for _ in range(n):
    a,b = input().split()
    peeps.append((a, int(b)))
mn = min([x[1] for x in peeps])
start = [x[1] for x in peeps].index(mn)
for i in range(start, start+n):
    print(peeps[i%n][0])
