class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        benches = defaultdict(set)
        for s, b in students:
            benches[b].add(s)
        return max([len(v) for k,v in benches.items()], default=0)