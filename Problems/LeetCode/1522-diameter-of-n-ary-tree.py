"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        parents = {}

        q = deque([(root, root)])
        while q:
            curr, p = q.popleft()
            parents[curr] = p

            for child in curr.children:
                q.append((child, curr))


        q = deque([curr])
        seen = set()
        steps = -1
        while q:
            steps += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr in seen: continue
                seen.add(curr)

                if parents[curr] not in seen:
                    q.append(parents[curr])
                for child in curr.children:
                    if child not in seen:
                        q.append(child)
        return steps
