class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        numsecs = 0
        total = sum(arr)
        if total%3!= 0: return False
        need = total//3
        section = 0
        for i, c in enumerate(arr):
            section += c
            if section == need: 
                section = 0
                numsecs += 1
                if numsecs == 3:
                    if sum(arr[i+1:]) ==0:
                        return True
        
        return False
