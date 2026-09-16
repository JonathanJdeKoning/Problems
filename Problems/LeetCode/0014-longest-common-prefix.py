class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return "".join([x[0] for x in takewhile(lambda z: len(set(z))==1, zip(*strs))])

