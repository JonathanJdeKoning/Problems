class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        mx = 0
        ans = 0
        currtime = 0
        for work in logs:
            timeworked = work[1]-currtime
            if timeworked > mx:
                mx = timeworked
                ans = work[0]
            if timeworked == mx:
                ans = min(ans, work[0])
            currtime = work[1]
        return ans