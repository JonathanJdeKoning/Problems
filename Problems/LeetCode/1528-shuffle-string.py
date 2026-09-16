class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ree = [None]*len(s)
        for i in range(len(s)):
            ree[indices[i]] = s[i]
        return "".join(ree)