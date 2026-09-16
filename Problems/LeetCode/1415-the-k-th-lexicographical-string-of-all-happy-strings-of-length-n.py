class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        allStrs = []
        mp = {"0": "a", "1":"b", "2":"c"}
        def ternary(num):
            if num == 0:
                return "a"*n
            nums = []
            while num:
                num, r = divmod(num, 3)
                nums.append(str(r))
            return ''.join(map(lambda c: mp[c], reversed(nums))).rjust(n, "a")
        
        currNum = 0
        currK = 1
        def good(s):
            return all([a!=b for a,b in pairwise(s)])
        while True:
            t = ternary(currNum)
            if len(t) > n: return ""
            if good(t) and len(t) == n:
                print(f"Good! T: {t}, K: {currK}")
                if currK == k:
                    return t
                currK += 1
            currNum += 1

