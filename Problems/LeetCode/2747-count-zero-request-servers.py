class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        def condition(idx, q):
            return allKeys[idx] > q

        ans = []
        timeAdd = defaultdict(set)
        timeDel = defaultdict(set)
        allKeys = set()
        for serverID, logTime in logs:
            allKeys.add(logTime)
            allKeys.add(logTime + x+1)

            timeAdd[logTime].add(serverID)
            timeDel[logTime+x+1].add(serverID)

        allKeys = sorted(allKeys)      
        times = {}
        currIDs = defaultdict(int)
        for time in allKeys:
            for delete in timeDel[time]:
                currIDs[delete] -= 1
                if currIDs[delete] <= 0:
                    del currIDs[delete]
            for add in timeAdd[time]:
                currIDs[add] += 1
            times[time] = n - len(currIDs)


        for q in queries:
            low = 0
            high = len(allKeys)

            while low < high:
                mid = (low+high) // 2
                if condition(mid, q):
                    high = mid
                else:
                    low = mid + 1

            ans.append(times[allKeys[low-1]])
        return ans
        







