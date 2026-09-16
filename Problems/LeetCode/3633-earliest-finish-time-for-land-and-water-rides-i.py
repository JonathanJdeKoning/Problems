class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        mnEnd = inf
        for i in range(len(landDuration)):
            landStart = landStartTime[i]
            lDuration = landDuration[i]
            landEnd = landStart + lDuration
            for j in range(len(waterDuration)):
                waterStart = waterStartTime[j]
                wDuration = waterDuration[j]

                waterEnter = max(waterStart, landEnd)
                endTime = waterEnter + wDuration
                mnEnd = min(mnEnd, endTime)

        for i in range(len(waterDuration)):
            waterStart = waterStartTime[i]
            wDuration = waterDuration[i]
            waterEnd = waterStart + wDuration
            for j in range(len(landDuration)):
                landStart = landStartTime[j]
                lDuration = landDuration[j]

                landEnter = max(landStart, waterEnd)
                endTime = landEnter + lDuration
                mnEnd = min(mnEnd, endTime)
                
        return mnEnd
        

        