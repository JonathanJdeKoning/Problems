class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = [x for x in list1 if x in list2]
        mn = inf
        out = []
        for c in common:
            sm = list1.index(c) + list2.index(c)
            if sm == mn:
                out.append(c)
            if sm < mn:
                out = [c]
                mn = sm
        return out