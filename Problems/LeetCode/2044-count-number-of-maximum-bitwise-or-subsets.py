class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def get_or(A):
            return (reduce(lambda x,y: x | y, A))
        mx = get_or(nums)
        ans = 0
        for i in range(2**len(nums)):
            x = bin(i)[2:].zfill(len(nums))
            t = []
            for i, c in enumerate(x):
                if c == '1':
                    t.append(nums[i])
            if not t: continue

            if get_or(t) == mx:
                ans += 1
        return ans
