class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefs = set()

        for num in arr1:
            tmp = str(num)
            for i in range(len(tmp)):
                prefs.add(tmp[:i+1])

        ans = 0
        for num in arr2:
            tmp = str(num)
            for i in range(len(tmp)):
                if tmp[:i+1] in prefs:
                    ans = max(ans, i+1)
        return ans

                    
                
                