class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalIndex = len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            mxIndex = i + nums[i]
            
            # If we can reach goalIndex
            if mxIndex >= goalIndex:
                goalIndex = i
                
        return goalIndex == 0
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # # Input: nums = [2,3,1,1,4]
            # # Output: true
            # # dp=[False], dp[0]=True
            # # dp[i]= True if dp[i-t for t in range(nums[n-t])] else False
            # if not nums:
            #     return False
            # if len(nums)==1:
            #     return True
            # dp=[False]*len(nums)
            # dp[0]=True
            # print(nums)
            # for i in range(nums[0]+1):
            #     dp[i]=True
            
            # cnt=0
            # while dp[-1]!=True:
            #     for i in range(len(nums)):
            #         if dp[i]==True:
            #             for k in range(nums[i]+1):
            #                 # print(k)
            #                 if i+k<len(nums):
            #                     dp[i+k]=True 
            #                 else:
            #                     pass
            #     cnt+=1
            #     if cnt>len(nums):
            #         break
            # # print(dp)
            # return dp[-1]==True
        
        
        