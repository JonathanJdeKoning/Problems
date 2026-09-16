class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:     
        q = deque()
        q.append(x)
        seen = set()
        steps = 0
        found = False
        while True:
            size = len(q)
            print(q)
            for _ in range(size):
                curr = q.popleft()
                if curr == y:
                    return steps
                if curr not in seen:
                    seen.add(curr)
                    if curr%11 == 0:
                        q.append(curr//11)
                    if curr%5 == 0:
                        q.append(curr//5)
                    if curr != 0:
                        q.append(curr-1)
                    if curr <= max(x,y)+13:
                        q.append(curr+1)
            steps += 1
 

