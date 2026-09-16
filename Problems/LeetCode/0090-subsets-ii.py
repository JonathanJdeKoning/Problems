class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        l = len(nums)
        for i in range(2**l):
            m = bin(i)[2:].zfill(l)
            x = []
            for j in range(l):
                if m[j] == "1":
                    x.append(nums[j])
            ans.add(tuple(x))
        return [list(x) for x in ans]