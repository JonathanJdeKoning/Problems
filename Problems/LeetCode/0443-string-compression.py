class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("###")
        chars.append("###")
        curr = 0
        currChar = chars[0]
        runlen = 1
        for i, c in enumerate(chars[1:], start=1):
            if i == len(chars)-1: break
            if c != currChar:
                chars[curr] = currChar
                if runlen != 1:
                    s = str(runlen)
                    for j in range(len(s)):
                        curr += 1
                        chars[curr] = s[j]
                curr += 1
                runlen = 1
                currChar = chars[i]
                continue
            else:
                runlen += 1
        return curr
