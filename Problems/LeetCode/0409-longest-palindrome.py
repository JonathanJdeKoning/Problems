class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        lens = list(Counter(s).values())
        try:
            mid = max([x for x in lens if x%2==1])
            lens.remove(mid)

        except:
            mid = 0
        lens = list(map(lambda x:x if x%2==0 else x-1,lens))

        return sum(lens)+mid