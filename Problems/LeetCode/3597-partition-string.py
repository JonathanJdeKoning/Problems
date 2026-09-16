class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        ans = []

        mark = 0
        for i in range(len(s)):
            chunk = s[mark:i+1]
            if chunk not in seen:
                seen.add(chunk)
                ans.append(chunk)
                mark = i+1
        return ans
