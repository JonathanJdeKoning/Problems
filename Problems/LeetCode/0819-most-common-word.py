class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = "".join(list(map(lambda x: x.lower() if x.isalpha() else " ", paragraph)))
        paragraph = paragraph.split()

        banned = set(banned)
        freq = defaultdict(int)

        for word in paragraph:
            freq[word] += 1
        
        mx = 0
        bestWord = paragraph[0]
        for word in paragraph:
            if word in banned:
                continue
            if freq[word] > mx:
                mx = freq[word]
                bestWord = word
        return bestWord


