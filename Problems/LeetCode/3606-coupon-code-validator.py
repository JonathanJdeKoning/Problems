class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        good = []
        valid = set(["electronics", "grocery", "pharmacy", "restaurant"])
        for i in range(len(code)):
            id = code[i]
            biz = businessLine[i]
            active = isActive[i]

            if not active: continue
            if not id: continue
            if biz not in valid: continue
            bad = [x for x in id if x != "_" and not x.isalnum()]
            if bad: continue
            good.append((id, biz))

        good = sorted(good, key=lambda x:(x[1], x[0]))
        return [x[0] for x in good]