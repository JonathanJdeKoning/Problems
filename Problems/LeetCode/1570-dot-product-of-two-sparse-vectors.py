class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = {i:nums[i] for i in range(len(nums))}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.mp[i] * vec.mp[i] for i in set(self.mp.keys()).intersection(set(vec.mp.keys())))


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)