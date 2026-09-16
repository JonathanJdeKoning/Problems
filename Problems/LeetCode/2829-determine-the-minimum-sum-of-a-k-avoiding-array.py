class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans = []
        curr = 1
        while len(ans) != n:
            for num in ans:
                if num+curr == k:
                    break
            else:
                ans.append(curr)
            curr += 1
        return sum(ans)