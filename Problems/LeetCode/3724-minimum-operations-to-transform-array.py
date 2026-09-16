class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        closest = nums1[0]
        bugger = nums2[-1]
        for a,b in zip(nums1, nums2):
            ans += abs(a - b)
            if bugger > min(a,b) and bugger < max(a,b):
                closest = bugger
            else:
                mnDist = abs(min(a,b) - bugger)
                mxDist = abs(max(a,b) - bugger)
                if mnDist < mxDist and abs(closest - bugger) > mnDist:
                    closest = min(a,b)
                elif mxDist <= mnDist and abs(closest - bugger) > mxDist:
                    closest = max(a,b)
        ans += 1 + abs(closest-bugger)
        return ans
            