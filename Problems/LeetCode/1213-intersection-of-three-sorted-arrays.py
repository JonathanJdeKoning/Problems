class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        A = set(arr1)
        B = set(arr2)
        C = set(arr3)
        return sorted(A.intersection(B.intersection(C)))