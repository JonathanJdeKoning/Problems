class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def forceIsPossible(force):
            mym = m
            base = position[0]
            mym -= 1

            for p in position[1:]:
                if p - base < force: continue
                else:
                    mym -= 1
                    base = p
                    if mym == 0: return True
            return False

        return bisect_left(range(1, max(position)+1), True, key=lambda x: not forceIsPossible(x))