class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = senate.count("R")
        d = senate.count("D")
        q = deque(list(senate))

        swing = 0
        while True:
            if d == 0: return "Radiant"
            if r == 0: return "Dire"

            curr = q.popleft()

            if curr == "R":
                if swing < 0:
                    r -= 1
                    swing += 1
                    continue
                else:
                    swing += 1
                    q.append(curr)
            elif curr == "D":
                if swing > 0:
                    d -= 1
                    swing -= 1
                    continue
                else:
                    swing -= 1
                    q.append(curr)


