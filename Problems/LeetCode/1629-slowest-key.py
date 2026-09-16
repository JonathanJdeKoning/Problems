class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes = [0] + releaseTimes

        mx = 0
        key = None
        for i in range(len(releaseTimes)-1):
            letter = keysPressed[i]
            time = releaseTimes[i+1]-releaseTimes[i]
            if time > mx:
                mx = time
                key = letter
            elif time == mx:
                if letter > key:
                    key = letter
        return key