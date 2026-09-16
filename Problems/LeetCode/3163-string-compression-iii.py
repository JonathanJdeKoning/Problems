class Solution:
    def compressedString(self, word: str) -> str:
        g = groupby(word)
        ans = []
        for k, v in g:
            v = list(v)
            n = len(v)
            while n > 9:
                n -= 9
                ans.append(f"9{k}")
            ans.append(f"{n}{k}")
        return "".join(ans)
