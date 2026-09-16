class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        l = nums[0] + nums[1]
        r = nums[-1] + nums[-2]
        m = nums[0] + nums[-1]
        @cache
        def recurse(arr, score):
            if len(arr) < 2: return 0
            if len(arr) == 2 and arr[0]+arr[1] == score: return 1
            
            left = arr[0]+arr[1]
            mid = arr[0]+arr[-1]
            right = arr[-1]+arr[-2]
            
            poss = []
            if left == score:
                poss.append(1 + recurse(arr[2:], score))
            if mid == score:
                poss.append(1 + recurse(arr[1:-1], score))
            if right == score:
                poss.append(1 + recurse(arr[:-2], score))
            if poss:
                return max(poss)
            else:
                return 0
        
        cp = nums[:]
        one = recurse(tuple(cp), l)
        two = recurse(tuple(cp), r)
        three = recurse(tuple(cp), m)
        return max([one,two,three])
                
            

        