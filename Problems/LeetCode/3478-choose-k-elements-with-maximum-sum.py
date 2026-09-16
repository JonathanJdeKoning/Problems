class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N = len(nums1)
        ans = [None] * N

        mp = defaultdict(list)

        for i, a in enumerate(nums1):
            mp[a].append(i)

        h = []
        curr = 0 
        for q in sorted(mp.keys()):
            toAdd = 0
            for i in mp[q]:
                ans[i] = curr
                heappush(h, nums2[i])
                toAdd += nums2[i]
            curr += toAdd
            while len(h) > k:
                curr -= heappop(h)
        return ans

