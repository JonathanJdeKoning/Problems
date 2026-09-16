class Solution:
    def minimumSum(self, num: int) -> int:
        x = sorted(list(str(num)))
        return 10*int(x[0])+10*int(x[1])+int(x[2])+int(x[3])