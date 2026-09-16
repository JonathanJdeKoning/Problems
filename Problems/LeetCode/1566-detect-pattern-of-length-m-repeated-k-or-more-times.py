class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        good = False
        check =[]
        for i in range(len(arr)-(m-1)):
            check.append(arr[i:i+m])
        for c in check:
            print(c*k)
            if "-".join([str(x) for x in c*k]) in "-".join(str(x) for x in arr): return True
        return False
