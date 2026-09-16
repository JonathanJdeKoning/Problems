class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        fq = Counter(s)
        used = False
        for k, v in fq.items():
            if v % 2==1:
                if not used:
                    used = True
                else:
                    return False
        return True