class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        fq = Counter()
        for word in words:
            fq += Counter(list(word))
        return all(map(lambda x: fq[x]%len(words)==0, list(fq.keys())))