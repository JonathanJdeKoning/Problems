class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x%2==0]
        odds = [x for x in nums if x%2!=0]
        ans = []
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even.pop())
            else:
                ans.append(odds.pop())
        return ans