class Solution:
    def maxProduct(self, words: List[str]) -> int:
        w = [set(list(ww)) for ww in words]
        ans = 0
        for i in range(len(words)-1):
            a = w[i]
            for j in range(i+1, len(words)):
                b = w[j]
                if not a.intersection(b):
                    ans = max(ans, len(words[i]*len(words[j])))
        return ans
