class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        count = dict(Counter(s))
        mx = max(list(count.values()))
        goods = []
        for k, v in count.items():
            if v == mx:
                goods.append(k)
        brother = []
        for c in s[::-1]:
            if c in goods:
                brother.append(c)
                goods.remove(c)
        return "".join(brother[::-1])
        
                    
        