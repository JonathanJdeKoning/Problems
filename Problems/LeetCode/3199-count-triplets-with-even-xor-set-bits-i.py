class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        ans = 0
        for i in a:
            for j in b:
                for k in c:
                    if bin(i^j^k).count("1") %2 == 0:
                        ans += 1
        return ans