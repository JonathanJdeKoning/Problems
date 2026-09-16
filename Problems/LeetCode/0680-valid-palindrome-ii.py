class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        start = 0
        end = len(s)-1

        while end >= start:
            if s[end] != s[start]:
                str1 = s[:start]+s[start+1:]
                str2 = s[:end]+s[end+1:]

                if str1 == str1[::-1] or str2 == str2[::-1]:
                    return True
                else:
                    return False
            end -= 1
            start += 1

            