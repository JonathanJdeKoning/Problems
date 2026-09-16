class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        c = sum(1 for c in words[0] if c in "aeiou")
        for i in range(1, len(words)):
            if sum(1 for c in words[i] if c in "aeiou") == c:
                words[i] = words[i][::-1]
        return " ".join(words)