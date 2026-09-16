class Solution:
    def maximum69Number (self, num: int) -> int:
        new = ""
        beep = False
        for c in str(num):
            if c == "6" and not beep:
                new += "9"
                beep = True
            else:
                new += c
        return int(new)