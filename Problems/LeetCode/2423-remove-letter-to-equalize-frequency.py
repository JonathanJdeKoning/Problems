class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = list(Counter(word).values())
        count.sort()
        ff = dict(Counter(count))
        if len(ff) == 2 and ff.get(1,0) == 1: return True
        if len(count) == 1: return True
        if abs(count[0] - count[-1]) > 1: return False
        start = count[0] 
        wack = 0
        if count.count(1) == len(count): return True
        for num in count[1:]:
            if num == start+1 or num == start-1:
                wack +=1
            if num > start+1 or num <start-1: return False
        if wack != 1: return False
        return True