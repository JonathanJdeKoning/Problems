class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = []
        for word in words:
            diff = []
            for i in range(len(word)-1):
                diff.append(ord(word[i+1])-ord(word[i]))
            diffs.append(diff)
        a,b = diffs[0:2]
        if a==b:
            for i,diff in enumerate(diffs[2:],start=2):
                if diff != a: 
                    return words[i]
        return words[0] if diffs[2] != a else words[1]



                