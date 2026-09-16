# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        q = deque([root])
        while q:
            curr = q.popleft()
            if not curr: continue
            l = curr.left
            r = curr.right
            if l:
                adj[curr.val].append(l.val)
                adj[l.val].append(curr.val)
                q.append(l)
            
            if r:
                adj[curr.val].append(r.val)
                adj[r.val].append(curr.val)
                q.append(r)
        q = deque([start])
        steps = -1
        seen = set()
        while q:
            steps += 1
            for _ in range(len(q)):
                curr = q.popleft()
                seen.add(curr)
                for node in adj[curr]:
                    if node not in seen:
                        q.append(node)
                        seen.add(node)
        return steps

            