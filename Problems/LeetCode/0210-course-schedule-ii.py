from graphlib import TopologicalSorter
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {k:[] for k in range(numCourses)}
        for u,v in prerequisites:
            edges[u].append(v)
        try:
            order = list(TopologicalSorter(edges).static_order())
            return order
        except: return []
