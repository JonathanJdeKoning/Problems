class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        return sum_impl(n, edges)

def dfs_subtree_size(tree, u, subtree_size, depth):
    k = 1
    val = depth[u] + 1
    for v in tree[u]:
        if depth[v] is None:
            depth[v] = val
            k += dfs_subtree_size(tree, v, subtree_size, depth)
    subtree_size[u] = k
    return k

def dfs_sum(tree, u, d_subtree, dist):
    val = dist[u] + len(tree)
    for v in tree[u]:
        if dist[v] is None:
            dist[v] = val - 2 * d_subtree[v]
            dfs_sum(tree, v, d_subtree, dist)

def sum_impl(n, edges):
    assert len(edges) == n - 1
    if not edges:
        return [0]
    tree = [list() for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    subtree_size = [None] * n
    depth = [None] * n
    depth[0] = 0
    dfs_subtree_size(tree, 0, subtree_size, depth)
    dist = [None] * n
    dist[0] = sum(depth)
    dfs_sum(tree, 0, subtree_size, dist)
    return dist