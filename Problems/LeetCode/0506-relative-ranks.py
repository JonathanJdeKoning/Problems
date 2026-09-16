class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tups = []
        for i, c in enumerate(score):
            tups.append((c,i))
        tups = sorted(tups, reverse=True)
        gold = tups[0]
        score[gold[1]] = "Gold Medal"
        try:
            silver = tups[1]
            score[silver[1]] = "Silver Medal"
        except: return score
        try:
            bronze = tups[2]
            score[bronze[1]] = "Bronze Medal"
        except:
            return score
        
        for i in range(3,len(tups)):
            tup = tups[i]
            score[tup[1]] = str(i+1)
        return score
