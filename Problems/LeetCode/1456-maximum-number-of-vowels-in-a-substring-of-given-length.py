class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        left = 0
        right = k

        currVowels = 0
        for i in range(left, right):
            if s[i] in vowels: currVowels += 1


        maxVowels = currVowels
        while True:
            
            if s[left] in vowels:
                currVowels -= 1
            left += 1

            right += 1

            if right-1 == len(s): break

            if s[right-1] in vowels:
                currVowels += 1
            
            maxVowels = max(maxVowels, currVowels)

        return maxVowels
            

