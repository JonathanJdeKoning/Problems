class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + 1
            if digits[i] != 10: break
            digits[i] = 0

        if digits[0] == 0:
            return [1] + digits
        return digits