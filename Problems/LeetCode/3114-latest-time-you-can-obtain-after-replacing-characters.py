class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if s[-1] == "?":
            s[-1] = "9"
        if s[-2] == "?":
            s[-2] = "5"

        if s[0] == "?" and s[1] == "?":
            s[0] = "1"
            s[1] = "1"

        if s[0] == "?":
            if s[1] in "01":
                s[0] = "1"
            else:
                s[0] = "0"
        
        if s[1] == "?":
            if s[0] == "0":
                s[1] = "9"
            else:
                s[1] = "1"
        return "".join(s)

            