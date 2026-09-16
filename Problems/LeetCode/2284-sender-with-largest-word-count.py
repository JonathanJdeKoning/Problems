class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        wc = defaultdict(int)

        for msg, nme in zip(messages, senders):
            wc[nme] += len(msg.split())

        mx = max(wc.values())
        n = ""
        for k,v in wc.items():
            if v == mx: n = max(n, k)
        return n