class Solution:
    def reorderSpaces(self, text: str) -> str:
        sp = text.count(" ")
        words = text.split()
        gaps = len(words)-1
        if gaps == 0: return text.strip() + " "*sp
        fill = sp//gaps
        left = sp%gaps
        return (fill*" ").join(words) + " "*left