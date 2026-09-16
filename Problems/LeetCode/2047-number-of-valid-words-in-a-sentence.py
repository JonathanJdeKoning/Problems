class Solution:
    def countValidWords(self, sentence: str) -> int:
        valid = 0
        punc = " !.,"
        for word in sentence.split():
            if "-" in word:
                if word.count("-")>1:continue
                idx = word.index("-")
                if idx == 0 or idx == len(word)-1: continue
                if not word[idx-1].islower() or not word[idx+1].islower(): continue
            
            allpunc = [x for x in word if x in punc]
            if len(allpunc)>1: continue
            if len(allpunc)==1:
                if word[-1] != allpunc[0]: continue
            if len([x for x in word if x.isdigit()])!= 0: continue
            valid += 1
        return valid