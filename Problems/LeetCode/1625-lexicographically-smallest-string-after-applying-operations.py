class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        
        q = deque([deque(list(s))])
        seen = set()

        while q:
            curr = q.popleft()
            string = "".join(list(curr))
            if string in seen: continue
            seen.add(string)

            added = deque([str((int(x)+a)%10) if i%2 == 1 else x for i,x in enumerate(string)])
            if "".join(list(added)) not in seen:
                q.append(added)

            curr.rotate(b)

            if "".join(list(curr)) not in seen:
                q.append(curr)
        return min(seen)



        
