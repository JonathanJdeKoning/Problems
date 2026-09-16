class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for word in words[left:right+1]:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                count += 1
        return count