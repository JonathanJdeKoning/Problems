class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand.sort()
        
        count = dict(Counter(hand))

        for j in range(len(hand)//groupSize):
            mn = min(count.keys())

            for i in range(mn, mn+groupSize):
                if count.get(i, 0) == 0: return False
                else: 
                    count[i] -= 1
                    if count[i] == 0:
                        del count[i]
        return True
