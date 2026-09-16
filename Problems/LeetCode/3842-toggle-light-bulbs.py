class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        b = [False]*100

        for x in bulbs:
            xx = x - 1
            b[xx] = not b[xx]

        ans = []
        for i in range(len(b)):
            if b[i]:
                ans.append(i+1)
        return ans