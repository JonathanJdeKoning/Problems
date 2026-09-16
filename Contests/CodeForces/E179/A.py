from heapq import heappop, heappush
def solve():
    N = int(input())
    heap = [0,0,0]

    steps = 0
    while heap != [N ,N, N]:
        curr = heappop(heap)
        allowed = min(heap) * 2 + 1
    
        heappush(heap, min(allowed, N))
        steps += 1

    return steps


for _ in range(int(input())):
    print(solve())