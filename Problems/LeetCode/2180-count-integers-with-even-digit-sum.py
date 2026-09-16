class Solution:
    def countEven(self, num: int) -> int:
        total = 0
        for i in range(1,num+1):
            if sum([int(x) for x in str(i)])%2==0:
                total += 1
        return total