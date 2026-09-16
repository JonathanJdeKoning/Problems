class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sH, sM, sS = map(int, startTime.split(":"))
        eH, eM, eS = map(int, endTime.split(":"))
        return (eS-sS) + 60*(eM-sM) + 3600 * (eH - sH)
        