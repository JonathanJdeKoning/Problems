class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j: continue
                if words[i] in words[j]:
                    out.add(words[i])
        return list(out)