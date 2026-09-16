class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastSeen = {}
        
        for i, num in enumerate(nums):
            if num not in lastSeen:
                lastSeen[num] = i
            else:
                if i-lastSeen[num] <= k:
                    return True
                else:
                    lastSeen[num] = i
        return False