class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        need = len(nums)//3

        freq = Counter(nums)

        out = []
        for k, v in freq.items():
            if v > need:
                out.append(k)
        return out