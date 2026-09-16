class Solution(object):
    def maxDistance(self, arrays):
        mn = arrays[0][0]
        mx = arrays[0][-1]
        mxdist = 0

        for arr in arrays[1:]:
            mxdist = max(mxdist, abs(arr[-1] - mn), abs(mx - arr[0]))
            mn = min(mn, arr[0])
            mx = max(mx, arr[-1])

        return mxdist