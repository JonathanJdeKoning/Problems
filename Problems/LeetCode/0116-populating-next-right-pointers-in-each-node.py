"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr)

                if curr.left:
                    q.append(curr.left)
                    q.append(curr.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None
        return root