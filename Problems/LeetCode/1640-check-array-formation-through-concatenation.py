class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        try:pieces = sorted(pieces, key=lambda x:arr.index(x[0]))
        except:return False
        return list(chain.from_iterable(pieces)) == arr