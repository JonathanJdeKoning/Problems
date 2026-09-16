from collections import deque
def solve():
    N = int(input())

    q = deque()

    for i in range(N, 0, -1):
        if i%2 ==0 :
            q.appendleft(i)
        else:
            q.append(i)
    return list(q)



for _ in range(int(input())):
    print(" ".join(map(str, solve())))