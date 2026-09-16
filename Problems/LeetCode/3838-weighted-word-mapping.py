class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = []
        a = list("abcdefghijklmnopqrstuvwxyz")[::-1]
        w = [sum([weights[ord(c)-97] for c in word]) for word in words]
        print(w)
        return "".join([a[x%26] for x in w])