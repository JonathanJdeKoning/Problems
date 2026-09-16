class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        mx = 1
        pos = None
        for i,num in enumerate(nums):
            if num%2==0 and num <=threshold:
                pos = i+1
                break
        if pos == None: return 0
        
        run = 1
        needOdd = 1
        while pos != len(nums):
            num = nums[pos]
            if num > threshold:
                run=0
                pos += 1
                
                continue
            if run==0:
                if num%2!=0:
                    pos += 1
                    continue
                else:
                    run = 1
                    pos +=1
                    needOdd = 1
                    continue
            else:
                if needOdd == num%2:
                    run += 1
                    mx = max(run,mx)
                    pos += 1
                    needOdd = abs((num%2)-1)
                    continue
                else:
                    run = abs(num%2-1)
                    pos += 1
                    needOdd = abs(num%2-1)
        mx = max(run,mx)
        return mx


        


