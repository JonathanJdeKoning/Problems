class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []

        mp = {
            1000: "M", 
            900: "CM", 
            500: "D", 
            400: "CD", 
            100: "C", 
            90:"XC", 
            50: "L", 
            40: "XL", 
            10: "X", 
            9: "IX", 
            5: "V", 
            4: "IV", 
            1: "I"}

        while num:
            for k, v in mp.items():
                if num >= k:
                    num -= k
                    ans.append(v)
                    break
        return "".join(ans)
