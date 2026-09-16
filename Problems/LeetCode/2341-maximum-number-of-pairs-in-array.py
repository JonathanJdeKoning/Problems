class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        totalpairs = 0
        totalleft = 0
        count = dict(Counter(nums)).items()
        for num, numcount in count:
            if numcount%2==0:
                totalpairs+= numcount//2
            else:
                totalpairs += (numcount-1)//2
                totalleft+= 1
        return[totalpairs, totalleft]