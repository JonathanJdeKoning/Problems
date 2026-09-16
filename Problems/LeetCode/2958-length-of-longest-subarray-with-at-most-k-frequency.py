class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        mxlen = 1
        post = 0
        postnum = nums[0]
    
        for i, num in enumerate(nums):
            d[num] += 1
            if d[num] > k:
                mxlen = max(mxlen, i-post)
                while postnum != num:
                    d[postnum] -= 1
                    post += 1
                    postnum = nums[post]
                d[postnum] -= 1
                post += 1
                postnum = nums[post]
        mxlen = max(mxlen, (i+1)-post)
        return mxlen

