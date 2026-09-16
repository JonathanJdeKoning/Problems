from operator import __add__
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        fq = reduce(__add__, [Counter(list(accumulate(row))[:-1]) for row in wall])

        if not fq.most_common(): return len(wall)
        return len(wall) - fq.most_common()[0][1]