class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        fq = Counter(nums[:k])
        
        l = 0
        r = k
        
        ans = []
        
        while r <= len(nums):
            arr = sorted(fq.items(), key = lambda x: (x[1], x[0]))
            print(arr)
            total = 0
            for _ in range(x):
                if not arr: break
                k, v = arr.pop()
                total += k*v
            ans.append(total)
            
            if r == len(nums): break
            fq[nums[l]] -= 1
            l += 1
            fq[nums[r]] += 1
            r += 1
        
            
        return ans
                
                
                