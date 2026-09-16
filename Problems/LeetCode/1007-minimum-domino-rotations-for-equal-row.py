class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        poss = set([1,2,3,4,5,6])

        for a, b in zip(tops, bottoms):
            poss = poss.intersection({a,b})
            print(poss)
        if not poss: return -1
        mp = {n: [0,0] for n in poss}
        ans = inf
        for p in poss:
            topNeed = 0
            botNeed = 0
            for a,b in zip(tops, bottoms):
                if a != p:
                    topNeed += 1
                if b != p:
                    botNeed += 1
            ans = min(ans, min(topNeed, botNeed))
        return ans
