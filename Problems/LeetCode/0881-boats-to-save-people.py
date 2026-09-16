class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        total = 0
        while l<=r:
            left,right = people[l],people[r]
            if l == r:
                return total + 1
            
            if left+right > limit:
                total += 1
                r -= 1
            else:
                total += 1
                l += 1
                r -= 1
        return total

