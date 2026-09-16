class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"

        words = [int(word[0] in vowels and word[-1] in vowels) for word in words]
        pref =[0] + list(accumulate(words))
        ans = []
        for l, r in queries:
            ans.append(pref[r+1] - pref[l])
        return ans