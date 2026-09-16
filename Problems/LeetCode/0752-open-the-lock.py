class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([[0,0,0,0]])
        turns = -1
        seen = set()
        while q:
            turns += 1
            for _ in range(len(q)):
                curr = q.popleft()
                s = "".join([str(x) for x in curr])
                if s in seen or s in deadends: continue
                if s == target: return turns
                seen.add(s)
    
                for i, wheel in enumerate(curr):
                    up = curr[:]
                    down = curr[:]
                    up[i] = (wheel+1)%10
                    down[i] = (wheel-1)%10
                    
                    if "".join([str(x) for x in up]) not in seen: q.append(up)
                    if "".join([str(x) for x in down]) not in seen: q.append(down)
        return -1



