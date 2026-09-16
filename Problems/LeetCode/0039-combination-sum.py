class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        curr = []
        candidates.sort()
        def backtrack(i, target):
            if i >= len(candidates): return
            val = candidates[i]
            if target == 0:
                ans.append(copy.copy(curr))
                return

            if target - val >= 0:
                
                curr.append(val)
                backtrack(i, target - val)
                curr.pop()

                backtrack(i+1, target)
        backtrack(0, target)
        return ans
