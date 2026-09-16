class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits.count(suits[0]) == len(suits): return "Flush"
        if 3 in Counter(ranks).values() or 4 in Counter(ranks).values(): return "Three of a Kind"
        return "Pair" if 2 in Counter(ranks).values() else "High Card"
