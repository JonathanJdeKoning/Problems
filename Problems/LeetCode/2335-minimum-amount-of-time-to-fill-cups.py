class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = 0
        while amount:
            amount = sorted([x for x in amount if x >0],reverse = True)
            if not amount: break

            if len(amount)==3:
                amount[0]-=1
                amount[1]-=1
                total += 1
            else:
                amount = [x-1 for x in amount]
                total += 1
        return total

