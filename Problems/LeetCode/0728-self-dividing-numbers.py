class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for i in range(left, right+1):
            good = True
            for dig in str(i):
                if dig == "0":
                    good = False 
                    break
                if i%int(dig)!=0: 
                    good = False
                    break
            if good: out.append(i)
        return out 