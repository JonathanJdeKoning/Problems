"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        q = deque([root])
        if not root: return 0
        while q:
            depth += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr: continue
                for child in curr.children:
                    if child:
                        q.append(child)
        return depth