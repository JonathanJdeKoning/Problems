class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        def mp(w):
            return w[1] + w[0]
        
        fq = Counter(words)

        ans = 0

        for word in fq:
            if mp(word) in words and word[0] != word[1]:
                ans += 2*min(fq[word], fq[mp(word)])
            if word[0] == word[1]:
                ans += (fq[word]//2) * 4
        for k,v in fq.items():
            if k[0] == k[1] and v % 2 == 1:
                ans += 2
                break
        return ans
