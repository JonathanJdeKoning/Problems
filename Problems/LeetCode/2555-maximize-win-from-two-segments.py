class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        fq = Counter(prizePositions)
        spots = [0] + list(fq.keys())
        pref = {0: 0}
        total = 0

        for key, val in fq.items():
            total += val
            pref[key] = total

        print(pref)
        
        bestBefore = {0:0}
        bestSoFar = 0
        mxScore = 0
        for endPoint in spots[1:]:
            optimalStart = endPoint - k
            closestStartIDX = max(bisect_left(spots, optimalStart) - 1, 0)
            closestStart = spots[closestStartIDX]
            segmentScore = pref[endPoint] - pref[closestStart]
            bestSoFar = max(bestSoFar, segmentScore)
            bestBefore[endPoint] = bestSoFar

            mxScore = max(mxScore, segmentScore + bestBefore[closestStart])
        return mxScore
