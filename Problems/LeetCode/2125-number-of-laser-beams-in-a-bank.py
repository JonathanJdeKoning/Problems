class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = 0
        ans = 0
        for row in bank:
            x = row.count("1")
            ans += x * last
            if x:
                last = x
        return ans

