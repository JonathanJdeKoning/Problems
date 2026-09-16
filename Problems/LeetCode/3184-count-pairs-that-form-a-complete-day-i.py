class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        total = 0
        for i in range(len(hours)):
            for j in range(i+1, len(hours)):
                if (hours[i]+hours[j])%24==0:
                    total += 1
        return total