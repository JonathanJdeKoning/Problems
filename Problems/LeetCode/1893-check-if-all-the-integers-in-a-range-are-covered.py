class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        good = []
        for start, end in ranges:
            good += list(range(start, end+1))
        
        check = list(range(left, right+1))
        for val in check:
            if val not in good: return False
        return True