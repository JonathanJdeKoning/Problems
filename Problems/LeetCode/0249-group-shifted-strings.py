class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        def shift(s):
            return "".join([chr((((ord(c) - 97)+1)%26)+97) for c in s])

        for s in strings:
            old = s
            while s[0] != "a":
                s = shift(s)
            d[s].append(old)

        return list(d.values())