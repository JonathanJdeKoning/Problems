class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = -1
        start = 0
        end = 3
        for i in range(len(num)-(end-1)):
            x = num[start:end]
            if x[0]==x[1] and x[1] == x[2]:
                mx = str(max(int(mx), int(x[0])))
            start += 1
            end += 1
        return mx*3 if mx != -1 else ""