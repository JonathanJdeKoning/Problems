class Solution:
    def minSteps(self, n: int) -> int:
        q = deque([(1, 0)])
        steps = -1
        seen = set()
        while q:
            steps += 1
            for _ in range(len(q)):
                curr, buff = q.popleft()
                if curr == n: return steps
                if curr > n: continue
                if (curr, buff) in seen: continue
                seen.add((curr, buff))
                
                q.append((curr+buff, buff))
                q.append((curr, curr))


