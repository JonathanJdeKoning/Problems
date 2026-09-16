class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        word = [ord(c) for c in word]
        mx = max(word)
        mxsize = len(word) - (numFriends - 1)
        best = [mx]
        bestidx = word.index(mx)
        for i,c in enumerate(word):
            if c!= mx:continue
            sub = word[i:min(len(word), i+mxsize)]
            for a,b in zip_longest(best, sub, fillvalue=-1):
                if b > a:
                    best = sub
                    break
                if a>b:
                    break
        return "".join([chr(c) for c in best])