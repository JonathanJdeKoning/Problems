from graphlib import TopologicalSorter
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for u,v in prerequisites:
            edges[u].append(v)
        try:
            order = list(TopologicalSorter(edges).static_order())
        except: return False
        return True