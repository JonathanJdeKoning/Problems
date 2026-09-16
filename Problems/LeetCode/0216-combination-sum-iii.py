class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        seen = set()
        nums = [1,2,3,4,5,6,7,8,9]
        ans = set()
        def backtrack(curr, build):
            
            if curr == 0 and len(build) == k:
                ans.add(tuple(sorted(build)))
                return
            if len(build) > k: return
            for num in nums:
                if num in seen or curr - num < 0:
                    continue

                seen.add(num)
                build.append(num)
                backtrack(curr - num, build)
                seen.discard(num)
                build.pop()


        backtrack(n, [])
        return [list(x) for x in ans]