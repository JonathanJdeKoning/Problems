class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        isConnected = defaultdict(dict)
        ans = 0
        for start, end in connections:
            isConnected[start][end] = True
            isConnected[end][start] = False

        seen = set()

        def dfs(root):
            nonlocal ans
            seen.add(root)
            for node, val in isConnected[root].items():
                if node not in seen:
                    if val: ans += 1
                    dfs(node)

        dfs(0)
        return ans