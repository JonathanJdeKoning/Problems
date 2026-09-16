class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if not queryIP: return "Neither"
        if ".." in queryIP or "::" in queryIP: return "Neither"
        if not (queryIP[0].isdigit() or queryIP[0] in "abcdefABCDEF"): return "Neither"
        if not (queryIP[-1].isdigit() or queryIP[-1] in "abcdefABCDEF"): return "Neither"

        if "." in queryIP:
            if ":" in queryIP: return "Neither"
            nums = queryIP.split(".")
            for num in nums:
                if num[0] == "0" and len(num) != 1: return "Neither"
                if [x for x in num if not x.isdigit()]: return "Neither"

            if len(nums) != 4: return "Neither"
            nums = list(map(int, nums))
            if [x for x in nums if x >255 or x <0]: return "Neither"
            
            return "IPv4"
        elif ":" in queryIP:
            if "." in queryIP: return "Neither"
            nums = queryIP.split(":")

            for num in nums:
                if len(num) > 4: return "Neither"
                if [x for x in num if not (x.isdigit() or x in "abcdefABCDEF")]:
                    print("IPV6 CHARS")
                    return "Neither"
            
            if len(nums) != 8: return "Neither"

            return "IPv6"
        return "Neither"