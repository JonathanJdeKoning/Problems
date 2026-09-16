class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)-1):
            a = words[i]
            for j in range(i+1, len(words)):
                b = words[j]
                if b.startswith(a) and b.endswith(a):
                    ans += 1
        return ans