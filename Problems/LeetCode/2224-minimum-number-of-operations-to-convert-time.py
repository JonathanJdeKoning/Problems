class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr = current.split(":")
        currMinutes = 60*int(curr[0]) + int(curr[1])

        corr = correct.split(":")
        corrMinutes = 60*int(corr[0]) + int(corr[1])

        amount = corrMinutes - currMinutes
        total = 0
        while amount != 0:
            total += 1
            if amount >= 60:
                amount -= 60
                continue
            if amount >= 15:
                amount -= 15
                continue
            if amount >= 5:
                amount -= 5
                continue
            if amount >=1:
                amount -= 1
                continue
        return total