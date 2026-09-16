class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        one = [list(v) for k,v in groupby(name)]
        two = [list(v) for k,v in groupby(typed)]
        if len(one) != len(two): return False
        for i, sec in enumerate(one):
            if sec[0] != two[i][0]: return False
            if len(two[i])< len(sec): return False
        return True