from collections import deque

def solve():
    N , M  = map(int, input().split())
    rooms = deque(sorted(list(map(int, input().split()))))
    
    while N:
        if len(rooms) == 1:
            print(*[rooms.pop()]*6)
            return
         
        classA = rooms.popleft()
        classB = rooms.pop()

        print(*[classA, classB]*3)
        if N == 1: return
        print(*[classB, classA]*3)
        
        N -= 2


for _ in range(int(input())):
    solve()