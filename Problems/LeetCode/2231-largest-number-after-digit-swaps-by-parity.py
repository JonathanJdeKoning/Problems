class Solution:
    def largestInteger(self, num: int) -> int:
        odds = sorted([x for x in str(num) if int(x)%2==1])
        eves = sorted([x for x in str(num) if int(x)%2==0])
        new = []
        for c in str(num):
            if int(c)%2==0:
                new.append(eves.pop())
            else:
                new.append(odds.pop())
        return int("".join([str(x) for x in new]))
