class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = Counter([x%24 for x in hours])
        total = 0
        seen = set()
        for num, x in count.items():
            
            if num == 0 or num == 12:
                total += (x*(x-1))//2
            else:
                other = 24 - num
                if other not in seen and num not in seen:
                    total += count[other]*x
                    seen.add(other)
                    seen.add(num)
        return total