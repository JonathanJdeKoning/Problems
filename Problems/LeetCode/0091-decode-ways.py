class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def waysDecode(s):
            if not s: return 1
            if s[0] == "0": return 0

            if len(s) == 1:
                return 1

      
            if int(s[:2]) <= 26:
                return waysDecode(s[2:]) + waysDecode(s[1:])
            else:
                return waysDecode(s[1:])

        return waysDecode(s)

