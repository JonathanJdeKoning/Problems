class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        buckets = sorted([len(word) for word in words])
        letters = list(Counter("".join(words)).values())
        odds = len([x for x in letters if x%2!=0])
        ct = odds
        if odds >= 1:
            for i, buck in enumerate(buckets):
                if buck%2!= 0:
                    odds -= 1
                    buckets[i] -= 1
                    if odds == 0:
                        break
        
            for i in range(len(letters)):
                if letters[i]%2!=0:
                    letters[i]-=1
                    ct -=1
                    if ct ==0:
                        break
        left = sum(letters)
        while True:
            yum = [x for x in buckets if x!= 0]
            if yum == []:
                break
            tofill = min(yum)
            idx = buckets.index(tofill)
            if left - tofill < 0:
                break
            else:
                left -= tofill
                buckets[idx] = 0
        return buckets.count(0)
        
            
                    
                    
                