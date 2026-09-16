class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return Counter([k for k,v in groupby(s)])["1"] <= 1