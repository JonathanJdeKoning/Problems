class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        h = [(1, start_node)]
        seen = set()
        d = defaultdict(list)

        for [u,v], w in zip(edges, succProb):
            d[u].append((v,w))
            d[v].append((u,w))

        while h:
            currWeight, currNode = heapq.heappop(h)

            if currNode in seen: continue
            seen.add(currNode)

            if currNode == end_node: return -currWeight

            for edgeNode, edgeWeight in d[currNode]:
                if edgeNode in seen: continue

                heapq.heappush(h, (-(abs(currWeight)*abs(edgeWeight)), edgeNode))
        return 0