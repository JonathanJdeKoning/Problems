class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        total =0 
        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    total += 1
            if ruleKey == "color":
                if item[1] == ruleValue:
                    total += 1
            if ruleKey == "name":
                if item[2] == ruleValue:
                    total += 1
        return total