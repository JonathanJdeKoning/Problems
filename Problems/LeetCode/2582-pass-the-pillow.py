class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr = 1
        back = False
        while time > 0:
            time -= 1
            if curr == n:
                back = True
                curr -=1
            elif curr == 1:
                back = False
                curr += 1
            else:
                curr = curr-1 if back else curr+1
        return curr
