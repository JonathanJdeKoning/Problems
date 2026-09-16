class Solution:
    def frequencySort(self, s: str) -> str:
        count = dict(sorted(dict(Counter(s)).items(), key=lambda x:x[1], reverse=True))
        dap = []
        for key, val in count.items():
            dap.append(key*val)
        return "".join(dap)

