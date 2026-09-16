class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powThrees = [3**i for i in range(15)]
        for mask in range(2**15):
            ans = 0
            for j in range(15):
                if (1<<j) & mask:
                    ans += powThrees[j]
            if ans == n: return True
        return False
