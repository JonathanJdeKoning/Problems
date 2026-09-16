from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = list(Counter(tasks).values())
        return sum([(x+2)//3 for x in count]) if 1 not in count else -1
