from heapq import heappush, heappop
N = int(input())
A = list(map(int, input().split()))

h = []
health = 0
for num in A:
    health += num
    heappush(h, num)
    while health < 0:
        health -= heappop(h)
print(len(h))


