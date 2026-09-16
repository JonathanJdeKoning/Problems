"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        if not node.neighbors:
            return Node(1)
        edges = defaultdict(list)

        seen = set()
        q = deque([node])
        while q:
            curr = q.popleft()
            if curr in seen: continue
            seen.add(curr)

            for child in curr.neighbors:
                edges[curr.val].append(child.val)
                if child not in seen:
                    q.append(child)
        start = Node(1)

        q = deque([start])
        seen = set()
        nodeMap = {1:start}
        while q:
            curr = q.popleft()
            if curr in seen: continue
            seen.add(curr)

            for child in edges[curr.val]:
                if child not in nodeMap:
                    nodeMap[child] = Node(child)
                curr.neighbors.append(nodeMap[child])
                if nodeMap[child] not in seen:
                    q.append(nodeMap[child])
        return nodeMap[1]