class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        d = defaultdict(list)
        answer = [-1]*(n)

        for start, end, dist in edges:
            d[start].append((end, dist))
            d[end].append((start, dist))


        seen = set()
        heap = [(0, 0)]

        while heap:
            currDist, currNode = heappop(heap)
            if currNode in seen: continue
            seen.add(currNode)

            answer[currNode] = currDist

            for edgeNode, edgeDist in d[currNode]:
                totalDist = edgeDist + currDist
                if edgeNode not in seen and totalDist < disappear[edgeNode]:
                    heappush(heap, (totalDist, edgeNode))
     
        return answer