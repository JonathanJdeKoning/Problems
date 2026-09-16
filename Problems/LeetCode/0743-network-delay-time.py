class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        minDist = {}

        for start, end, dist in times:
            edges[start].append((end, dist))

        seen = set()
        heap = [(0, k)]

        while heap:
            currDist, currNode = heappop(heap)
            if currNode in seen:
                continue
            
            seen.add(currNode)
            minDist[currNode] = currDist

            for edgeNode, edgeDist in edges[currNode]:
                if edgeNode not in seen:
                    heappush(heap, (edgeDist+currDist, edgeNode))

        for i in range(1, n+1):
            if i not in minDist: return -1
        
        return max(minDist.values())
                




        