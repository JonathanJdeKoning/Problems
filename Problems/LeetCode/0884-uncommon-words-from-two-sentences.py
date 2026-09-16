class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        new = s1.split()+s2.split()
        return [x for x in new if new.count(x) == 1]
