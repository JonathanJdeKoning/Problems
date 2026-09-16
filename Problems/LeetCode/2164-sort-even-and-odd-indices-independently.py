class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd =[]
        even = []
        new = []
        for i, x in enumerate(nums):
            if i%2==0:
                even.append(x)
            else:
                odd.append(x)
        odd = sorted(odd)
        even = sorted(even,reverse=True)
        for i in range(len(nums)):
            if i%2==0:
                new.append(even.pop())
            else:
                new.append(odd.pop())
        return new
