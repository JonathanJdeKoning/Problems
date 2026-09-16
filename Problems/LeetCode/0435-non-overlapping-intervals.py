class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        A = sorted(intervals)
        stack = []
        for s,e in A:
            while stack and e < stack[-1][-1]:
                stack.pop()
            stack.append((s, e))

        B = []
        for s, e in stack:
            if not B:
                B.append((s,e))
                continue
            if s >= B[-1][-1]:
                B.append((s,e))
                continue
        return len(intervals) - len(B)         
        


