class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        seen = set()
        for a in range(len(nums)):
            for b in range(len(nums)):
                for c in range(len(nums)):
                    for d in range(len(nums)):
                        if not(a < b and b < c and c < d): continue
                        if nums[a]+nums[b]+nums[c] == nums[d]:
                            seen.add((a,b,c,d))
        return len(seen)