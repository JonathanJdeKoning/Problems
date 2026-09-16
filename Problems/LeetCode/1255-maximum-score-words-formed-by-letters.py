class Solution:
    def maxScoreWords(self, w: List[str], l: List[str], s: List[int]) -> int:
        def f(i, l):
            if i < len(w):
                result = f(i+1, l)
                if (q:=Counter(w[i])) <= l:
                    result = max(result, sum(s[ord(c)-97]*q[c] for c in q) + f(i+1, l-q))

                return result

            return 0
        
        return f(0, Counter(l))