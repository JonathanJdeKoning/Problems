class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        REFRAME:
        Find the maximum length of a subarray with <= 2 unique elements

        OBSERVATIONS:
        - Monotonic (if subarray of size n exists, subarray of size n-1 exists)
        
        ATTEMPT:
            - Binary search on subarray length, and check for validity in linear time
        """
        if len(set(fruits)) <= 2: return len(fruits)
        def isValid(size):
            l = 0
            r = size
            fq = Counter(fruits[:size])
            while r < len(fruits) and len(fq.keys()) > 2:
                fq[fruits[l]] -= 1
                if fq[fruits[l]] == 0:
                    del fq[fruits[l]]
                l += 1
                fq[fruits[r]] += 1
                r += 1

            return len(fq.keys()) <= 2
            

        low = 1            #good
        high = len(fruits) #bad

        while high > low + 1:
            mid = (high + low)//2

            if isValid(mid):
                low = mid
            else:
                high = mid
        return low