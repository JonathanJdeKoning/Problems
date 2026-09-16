class Solution:
    def entityParser(self, text: str) -> str:
        mp = {
            "&quot;":'"',
            "&apos;":"'",
            "&gt;":">",
            "&lt;":"<",
            "&frasl;":"/",
            "&amp;":"&",
        }
        for k,v in mp.items():
            text = text.replace(k, v)
        return text