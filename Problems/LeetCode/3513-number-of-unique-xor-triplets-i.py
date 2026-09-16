class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while True:
            p = 2**i
            if n <= p:
                if n == p and n <3:
                    return p
                if n == p:
                    return p*2
                return p
            i += 1
